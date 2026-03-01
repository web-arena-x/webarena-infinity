import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find security label
    sec_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "security":
            sec_label = lbl
            break
    if sec_label is None:
        return False, "Could not find label 'security'."

    errors = []

    if sec_label.get("color") != "#000000":
        errors.append(f"Security label color is '{sec_label.get('color')}', expected '#000000'.")
    if sec_label.get("description") != "Critical security work":
        errors.append(f"Security label description is '{sec_label.get('description')}', expected 'Critical security work'.")

    sec_id = sec_label["id"]

    # Find Security Hardening epic
    sec_epic = None
    for e in state.get("epics", []):
        if e.get("title") == "Security Hardening":
            sec_epic = e
            break
    if sec_epic is None:
        return False, "Could not find epic 'Security Hardening'."

    # Check open issues in the epic that have the security label
    epic_sec_issues = [i for i in state.get("issues", [])
                       if i.get("epicId") == sec_epic["id"]
                       and i.get("status") == "open"
                       and sec_id in i.get("labels", [])]

    if len(epic_sec_issues) < 3:
        errors.append(f"Expected at least 3 open security-labeled issues in Security Hardening epic, found {len(epic_sec_issues)}.")

    for issue in epic_sec_issues:
        if issue.get("weight") != 13:
            errors.append(f"Issue '{issue.get('title')}' weight is {issue.get('weight')}, expected 13.")

    if errors:
        return False, " ".join(errors)

    return True, f"Security label updated and weight set to 13 on {len(epic_sec_issues)} issues."
