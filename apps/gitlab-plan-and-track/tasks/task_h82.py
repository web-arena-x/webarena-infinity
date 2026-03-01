import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # The unassigned open issue in Security Hardening is "Implement CSRF token rotation"
    issue = None
    for i in state.get("issues", []):
        if i.get("title") == "Implement CSRF token rotation":
            issue = i
            break
    if issue is None:
        return False, "Could not find issue 'Implement CSRF token rotation'."

    # Check Chen Wei assigned
    chen_wei = None
    for u in state.get("users", []):
        if u.get("name") == "Chen Wei":
            chen_wei = u
            break
    if chen_wei is None:
        errors.append("Could not find user 'Chen Wei'.")
    elif chen_wei["id"] not in issue.get("assignees", []):
        errors.append("Issue not assigned to Chen Wei.")

    # Check priority::high label present
    high_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "priority::high":
            high_label = lbl
            break
    if high_label is None:
        errors.append("Could not find 'priority::high' label.")
    elif high_label["id"] not in issue.get("labels", []):
        errors.append("Issue missing 'priority::high' label.")

    # Check priority::medium removed (scoped label replacement)
    med_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "priority::medium":
            med_label = lbl
            break
    if med_label and med_label["id"] in issue.get("labels", []):
        errors.append("Issue still has 'priority::medium' label (should be replaced by priority::high).")

    # Check Sprint 27
    sprint27 = None
    for it in state.get("iterations", []):
        if it.get("title") == "Sprint 27":
            sprint27 = it
            break
    if sprint27 is None:
        errors.append("Could not find iteration 'Sprint 27'.")
    elif issue.get("iterationId") != sprint27["id"]:
        errors.append(
            f"Issue iterationId is '{issue.get('iterationId')}', expected '{sprint27['id']}'."
        )

    if errors:
        return False, " ".join(errors)

    return True, (
        "CSRF token rotation issue assigned to Chen Wei, "
        "labeled priority::high, moved to Sprint 27."
    )
