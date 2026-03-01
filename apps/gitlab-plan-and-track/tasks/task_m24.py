import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find Security Hardening epic
    sec_epic = None
    for epic in state.get("epics", []):
        if epic.get("title") == "Security Hardening":
            sec_epic = epic
            break
    if sec_epic is None:
        return False, "Could not find epic 'Security Hardening'."

    # Find Compliance Automation epic
    comp_epic = None
    for epic in state.get("epics", []):
        if epic.get("title") == "Compliance Automation":
            comp_epic = epic
            break
    if comp_epic is None:
        return False, "Could not find epic 'Compliance Automation'."

    if comp_epic.get("parentEpicId") != sec_epic["id"]:
        return False, f"Epic 'Compliance Automation' parentEpicId is '{comp_epic.get('parentEpicId')}', expected '{sec_epic['id']}'."

    # Find CSRF token rotation issue
    csrf_issue = None
    for issue in state.get("issues", []):
        if issue.get("title") == "Implement CSRF token rotation":
            csrf_issue = issue
            break
    if csrf_issue is None:
        return False, "Could not find issue 'Implement CSRF token rotation'."

    if csrf_issue.get("epicId") != comp_epic["id"]:
        return False, f"CSRF issue epicId is '{csrf_issue.get('epicId')}', expected '{comp_epic['id']}'."

    return True, "Epic 'Compliance Automation' created as child of Security Hardening, and CSRF token rotation issue is linked to it."
