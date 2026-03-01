import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find the CSRF token rotation issue
    target_issue = None
    for issue in state.get("issues", []):
        if issue.get("title") == "Implement CSRF token rotation":
            target_issue = issue
            break
    if target_issue is None:
        return False, "Could not find issue 'Implement CSRF token rotation'."

    # Find Sprint 26 iteration
    sprint26 = None
    for iteration in state.get("iterations", []):
        if iteration.get("title") == "Sprint 26":
            sprint26 = iteration
            break
    if sprint26 is None:
        return False, "Could not find iteration 'Sprint 26'."

    if target_issue.get("iterationId") != sprint26["id"]:
        return False, f"Issue iterationId is '{target_issue.get('iterationId')}', expected '{sprint26['id']}'."

    # Find priority::high label
    lbl_high = None
    lbl_medium = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "priority::high":
            lbl_high = lbl
        elif lbl.get("title") == "priority::medium":
            lbl_medium = lbl

    if lbl_high is None:
        return False, "Could not find label 'priority::high'."

    issue_labels = target_issue.get("labels", [])

    if lbl_high["id"] not in issue_labels:
        return False, "Issue does not have the 'priority::high' label."

    if lbl_medium and lbl_medium["id"] in issue_labels:
        return False, "Issue still has the 'priority::medium' label (should have been replaced by scoped label)."

    return True, "CSRF token rotation issue assigned to Sprint 26 with priority::high label."
