import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find Platform Redesign epic
    platform_epic = None
    for e in state.get("epics", []):
        if e.get("title") == "Platform Redesign":
            platform_epic = e
            break
    if platform_epic is None:
        return False, "Could not find epic 'Platform Redesign'."

    # Find Technical Debt Cleanup epic
    td_epic = None
    for e in state.get("epics", []):
        if e.get("title") == "Technical Debt Cleanup":
            td_epic = e
            break
    if td_epic is None:
        return False, "Could not find epic 'Technical Debt Cleanup'."

    # Check parent
    if td_epic.get("parentEpicId") != platform_epic["id"]:
        return False, "Epic 'Technical Debt Cleanup' is not a child of 'Platform Redesign'."

    td_epic_id = td_epic["id"]

    # Find technical-debt label
    td_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "technical-debt":
            td_label = lbl
            break
    if td_label is None:
        return False, "Could not find label 'technical-debt'."

    # Find all issues with the technical-debt label
    td_issues = [i for i in state.get("issues", []) if td_label["id"] in i.get("labels", [])]
    if len(td_issues) < 2:
        return False, f"Expected at least 2 issues with 'technical-debt' label, found {len(td_issues)}."

    # Check each is assigned to the new epic
    errors = []
    for issue in td_issues:
        if issue.get("epicId") != td_epic_id:
            errors.append(f"Issue '{issue.get('title')}' with technical-debt label not assigned to Technical Debt Cleanup epic.")

    if errors:
        return False, " ".join(errors)

    return True, f"Epic 'Technical Debt Cleanup' created as child of Platform Redesign with {len(td_issues)} technical-debt issues."
