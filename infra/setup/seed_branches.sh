#!/usr/bin/env bash
# Pre-seed git branches for all environments.
# Run from the repo root on any machine with push access.
#
# Reads infra/env_manifest.jsonl to determine which docs folder each env gets.
# Each line: {"env_id": "linear-account-settings", "docs_path": "apps/user-manuals/linear/02-account"}
#
# Each branch inherits everything from main and adds:
#   - apps/{env_id}/               (stub directory where Claude generates the environment)
#   - .claudeignore                (hides irrelevant apps and docs from Claude Code)
#
# Nothing is deleted — .claudeignore ensures Claude Code only sees the reference
# app (apps/gitlab-org-management/), the relevant product docs, and the env stub.
#
# Usage:
#   bash infra/setup/seed_branches.sh                              # seed all envs in manifest
#   bash infra/setup/seed_branches.sh path/to/manifest.jsonl       # custom manifest

set -euo pipefail

MANIFEST="${1:-infra/env_manifest.jsonl}"
REFERENCE_APP="gitlab-org-management"

if [ ! -f "$MANIFEST" ]; then
  echo "ERROR: Manifest not found: $MANIFEST"
  echo "Each line should be: {\"env_id\": \"...\", \"docs_path\": \"apps/user-manuals/...\"}"
  exit 1
fi

TOTAL=$(wc -l < "$MANIFEST" | tr -d ' ')
echo "=== Seeding $TOTAL branches from $MANIFEST ==="
echo "    Reference app: apps/$REFERENCE_APP"

# Ensure we're on main and up to date
git checkout main
git pull origin main

# Collect all product names from apps/user-manuals/
ALL_PRODUCTS=()
for d in apps/user-manuals/*/; do
  ALL_PRODUCTS+=("$(basename "$d")")
done

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

  # Create the env stub directory
  mkdir -p "$ENV_DIR"
  echo "# Environment $BRANCH" > "$ENV_DIR/README.md"

  # Build .claudeignore to hide irrelevant apps and docs from Claude Code.
  # Extract the product name from docs_path (e.g., "apps/user-manuals/shopify/themes" -> "shopify")
  PRODUCT=$(echo "$DOCS_PATH" | cut -d'/' -f3)

  {
    echo "# Auto-generated — hide irrelevant apps and docs for this environment"
    echo ""
    echo "# Other generated apps (not the reference, not this env)"
    for app_dir in apps/*/; do
      app_name="$(basename "$app_dir")"
      [ "$app_name" = "$REFERENCE_APP" ] && continue
      [ "$app_name" = "user-manuals" ] && continue
      [ "$app_name" = "$ENV_ID" ] && continue
      echo "apps/$app_name/"
    done
    echo ""
    echo "# Other product docs (not the one for this env)"
    for product in "${ALL_PRODUCTS[@]}"; do
      [ "$product" = "$PRODUCT" ] && continue
      echo "apps/user-manuals/$product/"
    done
  } > .claudeignore

  git add "$ENV_DIR" .claudeignore
  git commit -m "Seed branch $BRANCH (docs: $DOCS_PATH)"
  git push origin "$BRANCH"

  # Return to main for next iteration
  git checkout main

  echo "  [$COUNT/$TOTAL] created $BRANCH (docs: $DOCS_PATH)"
done < "$MANIFEST"

echo "=== Done: $COUNT branches processed ==="
