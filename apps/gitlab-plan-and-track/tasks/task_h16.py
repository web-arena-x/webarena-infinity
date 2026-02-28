import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find user "Nina Kowalski"
    nina = None
    for user in state.get("users", []):
        if user.get("name") == "Nina Kowalski":
            nina = user
            break
    if nina is None:
        return False, "Could not find user 'Nina Kowalski'."
    nina_id = nina["id"]

    # Find epic "Frontend Modernization"
    frontend_epic = None
    for epic in state.get("epics", []):
        if epic.get("title") == "Frontend Modernization":
            frontend_epic = epic
            break
    if frontend_epic is None:
        return False, "Could not find epic 'Frontend Modernization'."
    frontend_epic_id = frontend_epic["id"]

    # Find ALL issues with epicId == frontend_epic_id
    epic_issues = []
    for issue in state.get("issues", []):
        if issue.get("epicId") == frontend_epic_id:
            epic_issues.append(issue)

    if len(epic_issues) == 0:
        return False, "No issues found in 'Frontend Modernization' epic."

    if len(epic_issues) < 8:
        return False, f"Expected at least 8 issues in 'Frontend Modernization' epic, found {len(epic_issues)}."

    # Check Nina is in EVERY issue's assignees
    not_assigned = []
    for issue in epic_issues:
        if nina_id not in issue.get("assignees", []):
            not_assigned.append(issue.get("title", issue.get("id")))

    if not_assigned:
        return False, f"Nina Kowalski is not assigned to these Frontend Modernization issues: {not_assigned}"

    return True, f"Nina Kowalski is assigned to all {len(epic_issues)} issues in the 'Frontend Modernization' epic."
