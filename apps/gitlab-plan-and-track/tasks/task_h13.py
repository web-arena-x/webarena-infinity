import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find label "sprint-goal"
    sprint_goal_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "sprint-goal":
            sprint_goal_label = lbl
            break
    if sprint_goal_label is None:
        return False, "Could not find label 'sprint-goal'."

    # Check label color
    if sprint_goal_label.get("color") != "#1aaa55":
        return False, f"Label 'sprint-goal' has color='{sprint_goal_label.get('color')}', expected '#1aaa55'."

    sprint_goal_id = sprint_goal_label["id"]

    # Find iteration "Sprint 26"
    sprint26 = None
    for iteration in state.get("iterations", []):
        if iteration.get("title") == "Sprint 26":
            sprint26 = iteration
            break
    if sprint26 is None:
        return False, "Could not find iteration 'Sprint 26'."
    sprint26_id = sprint26["id"]

    # Find ALL open issues with iterationId == Sprint 26's id
    sprint26_open_issues = []
    for issue in state.get("issues", []):
        if issue.get("iterationId") == sprint26_id and issue.get("status") == "open":
            sprint26_open_issues.append(issue)

    if len(sprint26_open_issues) == 0:
        return False, "No open issues found in 'Sprint 26'."

    # Expected count from seed data (issues 4, 7, 10, 13, 14, 17, 18, 22, 27, 28)
    if len(sprint26_open_issues) < 5:
        return False, f"Expected at least 5 open issues in Sprint 26, found {len(sprint26_open_issues)}."

    # Check sprint-goal label is in each open issue's labels
    errors = []
    for issue in sprint26_open_issues:
        if sprint_goal_id not in issue.get("labels", []):
            errors.append(issue.get("title", issue.get("id")))

    if errors:
        return False, f"These Sprint 26 open issues are missing the 'sprint-goal' label: {errors}"

    return True, f"Label 'sprint-goal' (#1aaa55) created and applied to all {len(sprint26_open_issues)} open issues in Sprint 26."
