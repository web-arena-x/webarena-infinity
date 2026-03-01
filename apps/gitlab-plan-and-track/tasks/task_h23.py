import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find the API v3 Migration epic
    api_epic = None
    for epic in state.get("epics", []):
        if epic.get("title") == "API v3 Migration":
            api_epic = epic
            break
    if api_epic is None:
        return False, "Could not find epic 'API v3 Migration'."
    epic_id = api_epic["id"]

    # Find the breaking-change label
    bc_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "breaking-change":
            bc_label = lbl
            break
    if bc_label is None:
        return False, "Could not find label 'breaking-change'."
    bc_id = bc_label["id"]

    # Find all open issues in the epic
    epic_issues = []
    for issue in state.get("issues", []):
        if issue.get("epicId") == epic_id and issue.get("status") == "open":
            epic_issues.append(issue)

    if len(epic_issues) < 2:
        return False, f"Expected at least 2 open issues in API v3 Migration epic, found {len(epic_issues)}."

    # Check each has the breaking-change label
    errors = []
    for issue in epic_issues:
        if bc_id not in issue.get("labels", []):
            errors.append(issue.get("title"))

    if errors:
        return False, f"These API v3 Migration issues are missing the 'breaking-change' label: {errors}"

    return True, f"All {len(epic_issues)} open issues in the API v3 Migration epic have the 'breaking-change' label."
