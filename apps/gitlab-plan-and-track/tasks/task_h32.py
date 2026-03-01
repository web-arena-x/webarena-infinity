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

    # Find users
    sarah = None
    marcus = None
    for user in state.get("users", []):
        if user.get("name") == "Sarah Chen":
            sarah = user
        elif user.get("name") == "Marcus Johnson":
            marcus = user
    if sarah is None:
        return False, "Could not find user 'Sarah Chen'."
    if marcus is None:
        return False, "Could not find user 'Marcus Johnson'."

    # Find priority::high label
    high_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "priority::high":
            high_label = lbl
            break
    if high_label is None:
        return False, "Could not find label 'priority::high'."

    # Find Sprint 28
    sprint28 = None
    for iteration in state.get("iterations", []):
        if iteration.get("title") == "Sprint 28":
            sprint28 = iteration
            break
    if sprint28 is None:
        return False, "Could not find iteration 'Sprint 28'."

    errors = []

    # Check assignees
    assignees = target_issue.get("assignees", [])
    if sarah["id"] not in assignees:
        errors.append("Sarah Chen not assigned.")
    if marcus["id"] not in assignees:
        errors.append("Marcus Johnson not assigned.")

    # Check priority label
    if high_label["id"] not in target_issue.get("labels", []):
        errors.append("Label 'priority::high' not applied.")

    # Check iteration
    if target_issue.get("iterationId") != sprint28["id"]:
        errors.append(f"Iteration is '{target_issue.get('iterationId')}', expected Sprint 28.")

    if errors:
        return False, " ".join(errors)

    return True, "CSRF token rotation issue assigned to Sarah Chen and Marcus Johnson, priority high, in Sprint 28."
