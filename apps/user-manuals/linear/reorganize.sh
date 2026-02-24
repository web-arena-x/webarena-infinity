#!/bin/zsh
# Reorganize Linear docs into section-based directories

DOCS_DIR="/Users/shuyanzh/workshop/research/mirror-mirror/linear/docs"

# Clean up any old flat files and partial directories
rm -f "$DOCS_DIR"/[0-9][0-9][0-9]-*.md
rm -rf "$DOCS_DIR"/[0-9][0-9]-*/

download_section() {
  local section_dir="$1"
  shift
  local pages=("$@")

  mkdir -p "$DOCS_DIR/$section_dir"

  local i=0
  for page in "${pages[@]}"; do
    i=$((i + 1))
    local num=$(printf "%02d" $i)
    local outfile="$DOCS_DIR/$section_dir/${num}-${page}.md"
    local url="https://linear.app/docs/${page}.md"

    (
      content=$(curl -sL "$url")
      if [[ -n "$content" ]] && [[ ${#content} -gt 10 ]]; then
        echo "$content" > "$outfile"
        echo "  ✓ $section_dir/${num}-${page}.md"
      else
        echo "  ✗ FAILED: $section_dir/$page"
      fi
    ) &
  done
}

echo "Downloading all Linear docs into section directories..."
echo ""

# --- Section 01: Getting Started ---
download_section "01-getting-started" \
  "start-guide" "conceptual-model" "get-the-app"

# --- Section 02: Account ---
download_section "02-account" \
  "profile" "account-preferences" "notifications" "security-and-access"

# --- Section 03: Your Sidebar ---
download_section "03-your-sidebar" \
  "inbox" "my-issues" "pulse" "pull-request-reviews" "favorites"

# --- Section 04: Teams ---
download_section "04-teams" \
  "teams" "private-teams" "sub-teams" "configuring-workflows"

wait

# --- Section 05: Issues ---
download_section "05-issues" \
  "creating-issues" "editing-issues" "assigning-issues" "select-issues" \
  "parent-and-sub-issues" "issue-templates" "issue-documents" \
  "comment-on-issues" "editor" "delete-archive-issues" \
  "customer-requests" "due-dates" "estimates" "issue-relations" \
  "labels" "priority" "sla" "private-issue-sharing"

wait

# --- Section 06: Projects ---
download_section "06-projects" \
  "projects" "initiative-and-project-updates" "project-milestones" \
  "project-overview" "project-documents" "project-graph" "project-status" \
  "project-labels" "project-notifications" "project-priority" \
  "project-dependencies" "project-templates"

# --- Section 07: Initiatives ---
download_section "07-initiatives" \
  "initiatives" "sub-initiatives"

# --- Section 08: Cycles ---
download_section "08-cycles" \
  "use-cycles" "update-cycles" "cycle-graph"

# --- Section 09: Releases ---
download_section "09-releases" \
  "releases"

wait

# --- Section 10: Views ---
download_section "10-views" \
  "board-layout" "timeline" "custom-views" "triage" "user-views" \
  "peek" "default-team-pages" "label-views" "search" "filters" \
  "display-options"

# --- Section 11: AI ---
download_section "11-ai" \
  "agents-in-linear" "mcp" "triage-intelligence" "ai-at-linear"

# --- Section 12: Integrations ---
download_section "12-integrations" \
  "integration-directory" "airbyte" "linear-asks" "discord" "figma" \
  "front" "github-integration" "gitlab" "google-sheets" "gong" \
  "intercom" "jira" "notion" "salesforce" "sentry" "slack" \
  "zapier" "zendesk"

wait

# --- Section 13: Analytics ---
download_section "13-analytics" \
  "dashboards" "insights" "exporting-data"

# --- Section 14: Administration ---
download_section "14-administration" \
  "workspaces" "login-methods" "invite-members" "members-roles" \
  "workspace-owner" "team-owner" "security" "saml-and-access-control" \
  "scim" "api-and-webhooks" "third-party-application-approvals" \
  "billing-and-plans" "changes-to-linears-pricing-plans" \
  "changes-to-user-roles-when-upgrading-to-enterprise" "audit-log"

wait

# --- Section 15: Import ---
download_section "15-import" \
  "import-issues" "jira-to-linear" "github-to-linear"

# --- Section 16: Best Practices ---
download_section "16-best-practices" \
  "triage-manage-unplanned-work" "team-issue-limit" "view-demos" \
  "beta-project-planning" "ops-and-marketing"

# --- Section 17: Guides ---
download_section "17-guides" \
  "how-to-use-linear" "how-to-use-linear-small-teams" \
  "how-to-use-linear-startups-mid-size-companies" \
  "how-to-use-linear-large-scaling-companies" \
  "joining-your-team-on-linear" "making-the-most-of-linear" \
  "making-the-most-of-linear-business" "jira-terminology-translated" \
  "linear-for-growth" "linear-for-product-managers" \
  "report-performance-issues"

# --- Section 18: Deprecated ---
download_section "18-deprecated" \
  "agents-api-deprecated" "github"

wait

echo ""
echo "============================="
echo "Download complete!"
echo ""

# Count results
total=$(find "$DOCS_DIR" -path "*[0-9][0-9]-*/*.md" | wc -l | tr -d ' ')
echo "Total files: $total"
echo ""

# Show directory structure
for dir in "$DOCS_DIR"/[0-9][0-9]-*/; do
  count=$(ls -1 "$dir"/*.md 2>/dev/null | wc -l | tr -d ' ')
  echo "  $(basename $dir)/ ($count files)"
done
