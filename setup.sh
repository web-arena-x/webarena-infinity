#!/usr/bin/env bash
# One-command local setup for mirror-mirror.
# Usage: bash setup.sh
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_ROOT"

echo "=== mirror-mirror setup ==="

# 1. Python dependencies
echo "Installing Python dependencies..."
uv sync

# 2. Playwright browser
echo "Installing Playwright Chromium..."
uv run python -m playwright install chromium

# 3. OS-level dependencies for Chromium
echo "Installing Chromium system dependencies (requires sudo)..."
sudo uv run python -m playwright install-deps chromium

echo ""
echo "Setup complete. You can now run evaluations:"
echo "  python evaluation/run_eval_parallel.py --model gemini --task-id task_e1 --workers 1 --web-app apps/<app>"
