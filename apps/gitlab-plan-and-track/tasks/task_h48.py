import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find API v3 Migration epic
    api_epic = None
    for e in state.get("epics", []):
        if e.get("title") == "API v3 Migration":
            api_epic = e
            break
    if api_epic is None:
        return False, "Could not find epic 'API v3 Migration'."

    # Find breaking-change label
    bc_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "breaking-change":
            bc_label = lbl
            break
    if bc_label is None:
        return False, "Could not find label 'breaking-change'."

    bc_id = bc_label["id"]

    # Workflow-scoped label IDs
    workflow_ids = set()
    for lbl in state.get("labels", []):
        if lbl.get("title", "").startswith("workflow::"):
            workflow_ids.add(lbl["id"])

    # Check all open issues in this epic
    epic_issues = [i for i in state.get("issues", [])
                   if i.get("epicId") == api_epic["id"] and i.get("status") == "open"]

    if len(epic_issues) < 3:
        return False, f"Expected at least 3 open issues in API v3 Migration epic, found {len(epic_issues)}."

    errors = []
    for issue in epic_issues:
        title = issue.get("title", "?")
        if bc_id not in issue.get("labels", []):
            errors.append(f"Issue '{title}' missing 'breaking-change' label.")
        for lid in issue.get("labels", []):
            if lid in workflow_ids:
                errors.append(f"Issue '{title}' still has a workflow-scoped label.")
                break

    if errors:
        return False, " ".join(errors)

    return True, f"'breaking-change' added and workflow labels removed from {len(epic_issues)} API v3 Migration issues."
