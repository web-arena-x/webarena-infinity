#!/usr/bin/env bash
# Quick evaluation launcher.
#
# Usage:
#   ./run_eval.sh                                  # defaults: gemini, 4 workers, apps/gmail
#   ./run_eval.sh --model claude --workers 8
#   ./run_eval.sh --web-app apps/gitlab-org-management --model gpt
#   ./run_eval.sh --difficulty easy
#   ./run_eval.sh --task-id task_e1
#
# All flags are passed through to run_eval_parallel.py.

set -euo pipefail

# Defaults (override via flags)
MODEL="gemini"
WORKERS=4
WEB_APP="apps/gmail"
BASE_PORT=8001

# Parse args — extract known defaults, pass everything through
EXTRA_ARGS=()
while [[ $# -gt 0 ]]; do
    case "$1" in
        --model)    MODEL="$2";    shift 2 ;;
        --workers)  WORKERS="$2";  shift 2 ;;
        --web-app)  WEB_APP="$2";  shift 2 ;;
        --base-port) BASE_PORT="$2"; shift 2 ;;
        *)          EXTRA_ARGS+=("$1"); shift ;;
    esac
done

cd "$(dirname "$0")"

echo "==> Evaluating: $WEB_APP | model=$MODEL | workers=$WORKERS | ports=$BASE_PORT-$((BASE_PORT + WORKERS - 1))"

python evaluation/run_eval_parallel.py \
    --model "$MODEL" \
    --workers "$WORKERS" \
    --web-app "$WEB_APP" \
    --base-port "$BASE_PORT" \
    "${EXTRA_ARGS[@]}"
