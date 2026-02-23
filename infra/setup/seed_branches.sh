#!/usr/bin/env bash
# Pre-seed git branches for all environments.
# Run from the repo root on any machine with push access.
#
# Reads infra/env_manifest.jsonl to determine which docs folder each env gets.
# Each line: {"env_id": "env-001", "docs_path": "apps/gitlab-org-management/docs/development/activitypub"}
#
# Each branch gets:
#   - apps/gitlab-org-management/  (reference implementation for Claude Code to learn from)
#   - apps/{parent_app}/docs/      (full docs tree for the source app, copied from main)
#   - apps/env-XXX/                (stub directory where Claude generates the environment)
#   - docs/                        (project-level guides)
#   - evaluation/                  (eval harness)
#   - All other apps are REMOVED so Claude Code only sees the reference.
#
# Usage:
#   bash infra/setup/seed_branches.sh                              # seed all envs in manifest
#   bash infra/setup/seed_branches.sh path/to/manifest.jsonl       # custom manifest

set -euo pipefail

MANIFEST="${1:-infra/env_manifest.jsonl}"
REFERENCE_APP="gitlab-org-management"

if [ ! -f "$MANIFEST" ]; then
  echo "ERROR: Manifest not found: $MANIFEST"
  echo "Each line should be: {\"env_id\": \"env-001\", \"docs_path\": \"apps/.../docs/topic\"}"
  exit 1
fi

TOTAL=$(wc -l < "$MANIFEST" | tr -d ' ')
echo "=== Seeding $TOTAL branches from $MANIFEST ==="
echo "    Reference app: apps/$REFERENCE_APP"

# Ensure we're on main and up to date
git checkout main
git pull origin main

COUNT=0
while IFS= read -r line; do
  # Skip empty lines
  [ -z "$line" ] && continue

  # Parse JSON fields (lightweight — no jq dependency required, but use it if available)
  if command -v jq &>/dev/null; then
    ENV_ID=$(echo "$line" | jq -r '.env_id')
    DOCS_PATH=$(echo "$line" | jq -r '.docs_path')
  else
    ENV_ID=$(echo "$line" | python3 -c "import sys,json; print(json.load(sys.stdin)['env_id'])")
    DOCS_PATH=$(echo "$line" | python3 -c "import sys,json; print(json.load(sys.stdin)['docs_path'])")
  fi

  BRANCH="$ENV_ID"
  ENV_DIR="apps/$ENV_ID"
  COUNT=$((COUNT + 1))

  # Skip if branch already exists on remote
  if git ls-remote --heads origin "$BRANCH" | grep -q "$BRANCH"; then
    echo "  [$COUNT/$TOTAL] skip $BRANCH (already exists)"
    continue
  fi

  git checkout -b "$BRANCH" main

  # Remove all apps except the reference implementation
  for app_dir in apps/*/; do
    app_name="$(basename "$app_dir")"
    if [ "$app_name" != "$REFERENCE_APP" ]; then
      git rm -rf "$app_dir"
    fi
  done

  # Create the env stub directory
  mkdir -p "$ENV_DIR"
  echo "# Environment $BRANCH" > "$ENV_DIR/README.md"

  # Copy full docs tree for the parent app from main into the branch.
  # e.g., docs_path "apps/shopify/docs/themes" -> restore all of "apps/shopify/docs/"
  PARENT_APP=$(echo "$DOCS_PATH" | cut -d'/' -f2)
  if [ "$PARENT_APP" != "$REFERENCE_APP" ]; then
    git checkout main -- "apps/$PARENT_APP/docs/"
  fi

  git add "$ENV_DIR"
  git commit -m "Seed branch $BRANCH (docs: $DOCS_PATH)"
  git push origin "$BRANCH"

  # Return to main for next iteration
  git checkout main

  echo "  [$COUNT/$TOTAL] created $BRANCH (docs: $DOCS_PATH)"
done < "$MANIFEST"

echo "=== Done: $COUNT branches processed ==="
