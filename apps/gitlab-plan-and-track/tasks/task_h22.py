import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find Backlog milestone
    backlog = None
    for ms in state.get("milestones", []):
        if ms.get("title") == "Backlog":
            backlog = ms
            break
    if backlog is None:
        return False, "Could not find milestone 'Backlog'."
    backlog_id = backlog["id"]

    # Check that no open issues have milestoneId == null
    unmilestoned = []
    for issue in state.get("issues", []):
        if issue.get("status") == "open" and issue.get("milestoneId") is None:
            unmilestoned.append(issue.get("title"))

    if unmilestoned:
        return False, f"These open issues still have no milestone: {unmilestoned}"

    # Verify that known originally-unmilestoned issues now have Backlog
    expected_titles = [
        "File upload fails silently for files > 50MB",
        "Implement retry mechanism for failed API calls",
        "Fix dropdown menu position clipping at viewport edges",
        "Fix typo in 404 error page message",
        "Add tooltip to truncated sidebar labels",
    ]

    for title in expected_titles:
        issue = next((i for i in state.get("issues", []) if i.get("title") == title), None)
        if issue is None:
            return False, f"Could not find issue '{title}'."
        if issue.get("milestoneId") != backlog_id:
            return False, f"Issue '{title}' milestoneId is '{issue.get('milestoneId')}', expected '{backlog_id}'."

    return True, f"All open issues without a milestone have been moved to Backlog."
