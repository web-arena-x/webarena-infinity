import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find issue "Emergency security patch"
    target_issue = None
    for issue in state.get("issues", []):
        if issue.get("title") == "Emergency security patch":
            target_issue = issue
            break
    if target_issue is None:
        return False, "Could not find issue 'Emergency security patch'."

    # Find label "priority::critical"
    critical_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "priority::critical":
            critical_label = lbl
            break
    if critical_label is None:
        return False, "Could not find label 'priority::critical'."
    critical_label_id = critical_label["id"]

    # Find label "security"
    security_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "security":
            security_label = lbl
            break
    if security_label is None:
        return False, "Could not find label 'security'."
    security_label_id = security_label["id"]

    # Find user "James O'Brien"
    james = None
    for user in state.get("users", []):
        if user.get("name") == "James O'Brien":
            james = user
            break
    if james is None:
        return False, "Could not find user 'James O'Brien'."
    james_id = james["id"]

    # Find user "Oliver Schmidt"
    oliver = None
    for user in state.get("users", []):
        if user.get("name") == "Oliver Schmidt":
            oliver = user
            break
    if oliver is None:
        return False, "Could not find user 'Oliver Schmidt'."
    oliver_id = oliver["id"]

    # Find milestone "v4.2 - Security Hardening"
    security_milestone = None
    for ms in state.get("milestones", []):
        if ms.get("title") == "v4.2 - Security Hardening":
            security_milestone = ms
            break
    if security_milestone is None:
        return False, "Could not find milestone 'v4.2 - Security Hardening'."
    security_ms_id = security_milestone["id"]

    # Validate all fields
    errors = []

    if target_issue.get("confidential") is not True:
        errors.append("Issue is not marked confidential.")

    issue_labels = target_issue.get("labels", [])
    if critical_label_id not in issue_labels:
        errors.append("Label 'priority::critical' not applied.")
    if security_label_id not in issue_labels:
        errors.append("Label 'security' not applied.")

    assignees = target_issue.get("assignees", [])
    if james_id not in assignees:
        errors.append("James O'Brien not assigned to issue.")
    if oliver_id not in assignees:
        errors.append("Oliver Schmidt not assigned to issue.")

    if target_issue.get("weight") != 2:
        errors.append(f"Issue weight is {target_issue.get('weight')}, expected 2.")

    if target_issue.get("milestoneId") != security_ms_id:
        errors.append("Issue is not in 'v4.2 - Security Hardening' milestone.")

    if target_issue.get("status") != "open":
        errors.append(f"Issue status is '{target_issue.get('status')}', expected 'open'.")

    if errors:
        return False, " ".join(errors)

    return True, "Confidential issue 'Emergency security patch' created with all required attributes."
