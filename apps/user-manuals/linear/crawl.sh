#!/bin/bash
# Crawl all Linear docs in order

DOCS_DIR="/Users/shuyanzh/workshop/research/mirror-mirror/linear/docs"

# All docs pages in sidebar navigation order
PAGES=(
  # Getting Started
  "start-guide"
  "conceptual-model"
  "get-the-app"
  # Account
  "profile"
  "account-preferences"
  "notifications"
  "security-and-access"
  # Your Sidebar
  "inbox"
  "my-issues"
  "pulse"
  "pull-request-reviews"
  "favorites"
  # Teams
  "teams"
  "private-teams"
  "sub-teams"
  "configuring-workflows"
  # Issues
  "creating-issues"
  "editing-issues"
  "assigning-issues"
  "select-issues"
  "parent-and-sub-issues"
  "issue-templates"
  "issue-documents"
  "comment-on-issues"
  "editor"
  "delete-archive-issues"
  # Issue Properties
  "customer-requests"
  "due-dates"
  "estimates"
  "issue-relations"
  "labels"
  "priority"
  "sla"
  # Projects
  "projects"
  "initiative-and-project-updates"
  "project-milestones"
  "project-overview"
  "project-documents"
  "project-graph"
  "project-status"
  "project-labels"
  "project-notifications"
  "project-priority"
  "project-dependencies"
  "project-templates"
  # Initiatives
  "initiatives"
  "sub-initiatives"
  # Cycles
  "use-cycles"
  "update-cycles"
  "cycle-graph"
  # Views
  "board-layout"
  "timeline"
  "custom-views"
  "triage"
  "user-views"
  "peek"
  "default-team-pages"
  "label-views"
  # Find and Filter
  "search"
  "filters"
  "display-options"
  # AI
  "agents-in-linear"
  "mcp"
  "triage-intelligence"
  "ai-at-linear"
  # Integrations
  "integration-directory"
  "airbyte"
  "linear-asks"
  "discord"
  "figma"
  "front"
  "github-integration"
  "gitlab"
  "google-sheets"
  "gong"
  "intercom"
  "jira"
  "notion"
  "salesforce"
  "sentry"
  "slack"
  "zapier"
  "zendesk"
  # Analytics
  "dashboards"
  "insights"
  "exporting-data"
  # Administration
  "workspaces"
  "login-methods"
  "invite-members"
  "members-roles"
  "security"
  "saml-and-access-control"
  "scim"
  "api-and-webhooks"
  "third-party-application-approvals"
  "billing-and-plans"
  "audit-log"
  # Practices
  "import-issues"
  "triage-manage-unplanned-work"
  "team-issue-limit"
  "view-demos"
  "beta-project-planning"
  "ops-and-marketing"
  # Guides
  "joining-your-team-on-linear"
  "making-the-most-of-linear"
  "jira-terminology-translated"
  "linear-for-growth"
  "making-the-most-of-linear-business"
  "how-to-use-linear"
  "how-to-use-linear-small-teams"
  "how-to-use-linear-large-scaling-companies"
  "how-to-use-linear-startups-mid-size-companies"
  "linear-for-product-managers"
  # Additional / Reference
  "agents-api-deprecated"
  "github"
  "github-to-linear"
  "jira-to-linear"
  "workspace-owner"
  "changes-to-user-roles-when-upgrading-to-enterprise"
  "team-owner"
  "changes-to-linears-pricing-plans"
  "releases"
  "private-issue-sharing"
  "report-performance-issues"
)

echo "Downloading ${#PAGES[@]} Linear docs pages..."

# Download in parallel (up to 10 concurrent)
i=0
for page in "${PAGES[@]}"; do
  i=$((i + 1))
  num=$(printf "%03d" $i)
  outfile="${DOCS_DIR}/${num}-${page}.md"
  url="https://linear.app/docs/${page}.md"

  # Download with curl in background, limit concurrency
  (
    content=$(curl -sL "$url")
    if [ -n "$content" ] && [ "$content" != "404" ]; then
      echo "$content" > "$outfile"
      echo "  ✓ ${num}-${page}.md"
    else
      echo "  ✗ FAILED: ${page}"
    fi
  ) &

  # Limit to 10 concurrent downloads
  if (( i % 10 == 0 )); then
    wait
  fi
done

wait
echo ""
echo "Done! Downloaded to ${DOCS_DIR}/"
echo "Total files: $(ls -1 ${DOCS_DIR}/*.md 2>/dev/null | grep -v crawl.sh | wc -l)"
