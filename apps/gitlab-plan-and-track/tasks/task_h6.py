import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find milestone "v4.0 - Platform Redesign"
    v40_milestone = None
    for ms in state.get("milestones", []):
        if ms.get("title") == "v4.0 - Platform Redesign":
            v40_milestone = ms
            break
    if v40_milestone is None:
        return False, "Could not find milestone 'v4.0 - Platform Redesign'."
    v40_id = v40_milestone["id"]

    # Check that v4.0 is closed
    if v40_milestone.get("status") != "closed":
        return False, f"Milestone 'v4.0 - Platform Redesign' is not closed (status='{v40_milestone.get('status')}')."

    # Find milestone "v4.1 - Performance"
    v41_milestone = None
    for ms in state.get("milestones", []):
        if ms.get("title") == "v4.1 - Performance":
            v41_milestone = ms
            break
    if v41_milestone is None:
        return False, "Could not find milestone 'v4.1 - Performance'."
    v41_id = v41_milestone["id"]

    # Open issues that were in v4.0 in seed data (by exact title)
    open_issue_titles = [
        "Migrate user settings page to React",
        "Build component library documentation site",
        "Implement GraphQL gateway for v3 API",
        "Login page shows blank screen on Safari 17.2",
        "Email notifications sent with wrong timezone offset",
        "Dashboard widget layout breaks at 1440px viewport",
        "Add dark mode support for the entire application",
        "Update project README with new setup instructions",
        "Add accessibility labels to all form inputs",
        "Improve error boundary fallback UI",
        "Replace deprecated analytics library",
        "Create reusable data table component with sorting and filtering",
    ]

    issues_by_title = {}
    for issue in state.get("issues", []):
        title = issue.get("title")
        if title in open_issue_titles:
            issues_by_title[title] = issue

    missing = [t for t in open_issue_titles if t not in issues_by_title]
    if missing:
        return False, f"Could not find expected open v4.0 issues: {missing}"

    # All open v4.0 issues should now be in v4.1
    wrong = []
    for title, issue in issues_by_title.items():
        if issue.get("milestoneId") != v41_id:
            wrong.append(title)

    if wrong:
        return False, f"These open v4.0 issues were not moved to 'v4.1 - Performance': {wrong}"

    return True, f"Milestone 'v4.0 - Platform Redesign' closed and all {len(open_issue_titles)} open issues moved to 'v4.1 - Performance'."
