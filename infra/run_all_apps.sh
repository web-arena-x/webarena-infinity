#!/usr/bin/env bash
# Run real-tasks evaluation across all apps sequentially for a given model.
# Default: 3 repetitions with failed-only cascade (same as pipeline phase 5).
#
# Usage:
#   bash infra/run_all_apps.sh --model gemini-pro --workers 8
#   bash infra/run_all_apps.sh --model kimi --workers 4 --tag full-sweep
#   bash infra/run_all_apps.sh --model claude --workers 8 --repetitions 1  # single run

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# --- Defaults ---
MODEL=""
WORKERS=8
REPETITIONS=3
TAG=""
EXTRA_ARGS=""

# --- Parse args ---
while [[ $# -gt 0 ]]; do
    case "$1" in
        --model)       MODEL="$2"; shift 2 ;;
        --workers)     WORKERS="$2"; shift 2 ;;
        --repetitions) REPETITIONS="$2"; shift 2 ;;
        --tag)         TAG="$2"; shift 2 ;;
        *)         EXTRA_ARGS="$EXTRA_ARGS $1"; shift ;;
    esac
done

if [[ -z "$MODEL" ]]; then
    echo "Error: --model is required (gemini-pro, gemini-flash, claude, kimi, gemini-cu, claude-cu)"
    exit 1
fi

# --- Discover apps with real-tasks.json ---
APPS=()
for app_dir in apps/*/; do
    if [[ -f "$app_dir/real-tasks.json" ]]; then
        APPS+=("$app_dir")
    fi
done

echo "============================================================"
echo "  All-Apps Evaluation"
echo "============================================================"
echo "  Model:   $MODEL"
echo "  Workers:     $WORKERS"
echo "  Repetitions: $REPETITIONS (failed-only cascade)"
echo "  Tag:         ${TAG:-<none>}"
echo "  Apps:    ${#APPS[@]}"
for app in "${APPS[@]}"; do
    echo "    - $(basename "$app")"
done
echo "============================================================"
echo ""

# --- Activate venv ---
if [ -d "$HOME/venv" ]; then
    source "$HOME/venv/bin/activate"
elif [ -d "$REPO_ROOT/.venv" ]; then
    source "$REPO_ROOT/.venv/bin/activate"
else
    echo "Error: No virtualenv found at ~/venv or $REPO_ROOT/.venv"
    exit 1
fi

PASSED=0
FAILED=0
ERRORS=()

for app in "${APPS[@]}"; do
    app_name="$(basename "$app")"
    echo "──────────────────────────────────────────────────────────"
    echo "  ▶ $app_name"
    echo "──────────────────────────────────────────────────────────"

    TAG_ARG=""
    if [[ -n "$TAG" ]]; then
        TAG_ARG="--tag $TAG"
    fi

    if python evaluation/run_eval_parallel.py \
        --model "$MODEL" \
        --workers "$WORKERS" \
        --web-app "$app" \
        --task-suite real-tasks \
        --repetitions "$REPETITIONS" \
        --failed-only \
        $TAG_ARG \
        $EXTRA_ARGS; then
        PASSED=$((PASSED + 1))
        echo "  ✓ $app_name completed"
    else
        FAILED=$((FAILED + 1))
        ERRORS+=("$app_name")
        echo "  ✗ $app_name failed (non-zero exit)"
    fi
    echo ""
done

echo "============================================================"
echo "  All-Apps Summary: $MODEL"
echo "============================================================"
echo "  Completed: $PASSED/${#APPS[@]}"
if [[ $FAILED -gt 0 ]]; then
    echo "  Errors:    $FAILED (${ERRORS[*]})"
fi
echo "============================================================"
