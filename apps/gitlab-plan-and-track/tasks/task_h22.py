import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find the Security Hardening epic
    epic = None
    for e in state.get("epics", []):
        if e.get("title") == "Security Hardening":
            epic = e
            break
    if epic is None:
        return False, "Could not find epic 'Security Hardening'."

    epic_id = epic["id"]

    # Find the issue that was unassigned in seed (CSRF token rotation)
    target_issue = None
    for issue in state.get("issues", []):
        if issue.get("title") == "Implement CSRF token rotation":
            target_issue = issue
            break
    if target_issue is None:
        return False, "Could not find issue 'Implement CSRF token rotation'."

    # Verify it belongs to the Security Hardening epic
    if target_issue.get("epicId") != epic_id:
        return False, "Issue 'Implement CSRF token rotation' is not in the Security Hardening epic."

    # Find Chen Wei
    chen_wei = None
    for user in state.get("users", []):
        if user.get("name") == "Chen Wei":
            chen_wei = user
            break
    if chen_wei is None:
        return False, "Could not find user 'Chen Wei'."

    # Check assignees
    if chen_wei["id"] not in target_issue.get("assignees", []):
        return False, "Chen Wei is not assigned to the CSRF token rotation issue."

    # Find Sprint 27
    sprint27 = None
    for iteration in state.get("iterations", []):
        if iteration.get("title") == "Sprint 27":
            sprint27 = iteration
            break
    if sprint27 is None:
        return False, "Could not find iteration 'Sprint 27'."

    # Check iteration
    if target_issue.get("iterationId") != sprint27["id"]:
        return False, f"Issue iteration is '{target_issue.get('iterationId')}', expected '{sprint27['id']}'."

    return True, "Unassigned issue in Security Hardening epic assigned to Chen Wei and moved to Sprint 27."
