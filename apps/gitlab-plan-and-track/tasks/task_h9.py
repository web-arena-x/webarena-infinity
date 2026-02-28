import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find milestone "Backlog"
    backlog_milestone = None
    for ms in state.get("milestones", []):
        if ms.get("title") == "Backlog":
            backlog_milestone = ms
            break
    if backlog_milestone is None:
        return False, "Could not find milestone 'Backlog'."
    backlog_id = backlog_milestone["id"]

    # Find label "needs-discussion"
    needs_discussion_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "needs-discussion":
            needs_discussion_label = lbl
            break
    if needs_discussion_label is None:
        return False, "Could not find label 'needs-discussion'."
    needs_discussion_id = needs_discussion_label["id"]

    # Expected unassigned open issue titles
    expected_titles = [
        "Implement CSRF token rotation",
        "Markdown preview renders incorrectly with nested code blocks",
        "Build real-time collaborative editing for issue descriptions",
        "Add custom fields support for issues",
        "Add webhook support for issue state changes",
        "Fix typo in 404 error page message",
        "Add tooltip to truncated sidebar labels",
        "Implement GitLab Pages custom domain support",
        "Add merge request approval rules engine",
        "Add inline code suggestions in merge request reviews",
    ]

    issues_by_title = {}
    for issue in state.get("issues", []):
        title = issue.get("title")
        if title in expected_titles:
            issues_by_title[title] = issue

    missing = [t for t in expected_titles if t not in issues_by_title]
    if missing:
        return False, f"Could not find expected unassigned issues: {missing}"

    # Check each has Backlog milestone and needs-discussion label
    errors = []
    for title, issue in issues_by_title.items():
        if issue.get("milestoneId") != backlog_id:
            errors.append(f"'{title}' not in Backlog milestone.")
        if needs_discussion_id not in issue.get("labels", []):
            errors.append(f"'{title}' missing 'needs-discussion' label.")

    if errors:
        return False, " ".join(errors)

    return True, f"All {len(expected_titles)} unassigned open issues moved to Backlog milestone with 'needs-discussion' label."
