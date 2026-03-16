#!/usr/bin/env bash
# Monitor eval progress across multiple EC2 instances.
#
# Usage:
#   bash infra/setup/monitor_eval.sh
#   bash infra/setup/monitor_eval.sh --once        # single snapshot, no loop
#   bash infra/setup/monitor_eval.sh --interval 60  # poll every 60s (default: 30)

set -euo pipefail

SSH_KEY="${SSH_KEY:-$HOME/.ssh/mirror-mirror.pem}"
INTERVAL=30
ONCE=false

while [[ $# -gt 0 ]]; do
    case "$1" in
        --once)     ONCE=true; shift ;;
        --interval) INTERVAL="$2"; shift 2 ;;
        --key)      SSH_KEY="$2"; shift 2 ;;
        *)          echo "Unknown arg: $1"; exit 1 ;;
    esac
done

# --- Instance registry ---
# Format: IP|MODEL|LOG_FILE
INSTANCES=(
    "100.49.217.160|gemini-cu|/tmp/mirror-mirror-logs/gemini-cu.log"
    "44.212.193.202|gemini-pro|/tmp/mirror-mirror-logs/gemini-pro.log"
    "98.87.74.215|kimi|/tmp/mirror-mirror-logs/kimi.log"
    "98.95.45.41|claude-cu|/tmp/mirror-mirror-logs/claude-cu.log"
)

SSH_OPTS="-i $SSH_KEY -o StrictHostKeyChecking=no -o ConnectTimeout=5 -o LogLevel=ERROR"

monitor_instance() {
    local ip="$1"
    local model="$2"
    local logfile="$3"

    # Try to connect
    if ! ssh $SSH_OPTS ec2-user@"$ip" "echo ok" &>/dev/null; then
        echo "  [$model] $ip — UNREACHABLE"
        return
    fi

    local status
    status=$(ssh $SSH_OPTS ec2-user@"$ip" "python3 -" "$logfile" <<'PYREMOTE'
import sys, os, re

logfile = sys.argv[1]
if not os.path.exists(logfile):
    print("NO_LOG")
    sys.exit(0)

with open(logfile, "r", errors="replace") as f:
    raw = f.read()

# Strip ANSI codes
clean = re.sub(r'\x1b\[[0-9;]*m', '', raw)
lines = clean.split('\n')

# Process is running?
import subprocess
r = subprocess.run(["pgrep", "-f", "run_all_apps"], capture_output=True)
running = "RUNNING" if r.returncode == 0 else "STOPPED"

# Current app
apps = [l.split('▶')[-1].strip().split()[0] for l in lines if '▶' in l]
current_app = apps[-1] if apps else "?"

# Completed apps
completed = sum(1 for l in lines if 'completed' in l and '✓' in l)
errored = sum(1 for l in lines if 'failed (non-zero' in l)

# Task counts
passed = sum(1 for l in lines if ' PASS ' in l)
failed = sum(1 for l in lines if ' FAIL ' in l)
timed = sum(1 for l in lines if ' TIME ' in l)

# Rate limit
rate_429 = sum(1 for l in lines if any(k in l.upper() for k in ['429', 'RESOURCE_EXHAUSTED', 'RATE LIMIT', 'TOO MANY REQUESTS']))

# Other errors
other_err = sum(1 for l in lines if re.search(r'error|exception|traceback', l, re.I) and not any(k in l.upper() for k in ['429', 'RESOURCE_EXHAUSTED', 'RATE LIMIT']))

# Last result
result_lines = [l.strip() for l in lines if any(k in l for k in [' PASS ', ' FAIL ', ' TIME '])]
last_result = result_lines[-1] if result_lines else ""

print(f"{running}|{current_app}|{completed}|{errored}|{passed}|{failed}|{timed}|{rate_429}|{other_err}|{last_result}")
PYREMOTE
    )

    if [ "$status" = "NO_LOG" ]; then
        echo "  [$model] $ip — log file not found (not started?)"
        return
    fi

    IFS='|' read -r running current_app completed errored pass fail timed rate_limit other_err last_result <<< "$status"

    # Default empty values to 0
    pass=${pass:-0}; fail=${fail:-0}; timed=${timed:-0}
    completed=${completed:-0}; errored=${errored:-0}
    rate_limit=${rate_limit:-0}; other_err=${other_err:-0}

    local total=$((pass + fail + timed))
    local sr="0.0"
    if [ "$total" -gt 0 ]; then
        sr=$(python3 -c "print(f'{$pass/$total*100:.1f}')")
    fi

    echo "  [$model] $ip"
    echo "    Status:      $running"
    echo "    Current app: $current_app"
    echo "    Apps done:   $completed ok, $errored errored"
    echo "    Tasks:       $pass pass / $fail fail / $timed timeout  (total: $total, SR: ${sr}%)"
    if [ "$rate_limit" -gt 0 ]; then
        echo "    ⚠ RATE LIMIT: $rate_limit occurrences"
    fi
    if [ "$other_err" -gt 0 ]; then
        echo "    Errors:      $other_err lines with error/exception"
    fi
    echo "    Last result: $last_result"
}

print_status() {
    echo "============================================================"
    echo "  Eval Monitor — $(date '+%Y-%m-%d %H:%M:%S')"
    echo "============================================================"
    echo ""

    for entry in "${INSTANCES[@]}"; do
        IFS='|' read -r ip model logfile <<< "$entry"
        monitor_instance "$ip" "$model" "$logfile"
        echo ""
    done

    echo "============================================================"
}

if [ "$ONCE" = true ]; then
    print_status
else
    while true; do
        clear
        print_status
        echo "  Refreshing every ${INTERVAL}s... (Ctrl+C to stop)"
        sleep "$INTERVAL"
    done
fi
