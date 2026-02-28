import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find milestone "v4.2 - Security Hardening"
    security_milestone = None
    for ms in state.get("milestones", []):
        if ms.get("title") == "v4.2 - Security Hardening":
            security_milestone = ms
            break
    if security_milestone is None:
        return False, "Could not find milestone 'v4.2 - Security Hardening'."
    security_ms_id = security_milestone["id"]

    # Find milestone "v4.1 - Performance"
    performance_milestone = None
    for ms in state.get("milestones", []):
        if ms.get("title") == "v4.1 - Performance":
            performance_milestone = ms
            break
    if performance_milestone is None:
        return False, "Could not find milestone 'v4.1 - Performance'."
    performance_ms_id = performance_milestone["id"]

    # Find label "security" by title
    security_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "security":
            security_label = lbl
            break
    if security_label is None:
        return False, "Could not find label 'security' in state."
    security_label_id = security_label["id"]

    # Among issues originally in Security Hardening, those WITHOUT the security label
    # should now be in v4.1 - Performance
    issues_without_security = []
    issues_with_security = []
    for issue in state.get("issues", []):
        ms_id = issue.get("milestoneId")
        issue_labels = issue.get("labels", [])
        # We need to check issues that were moved (now in performance) or still in security
        # The task was: move issues in Security Hardening WITHOUT security label to v4.1
        # After the task, issues without security label should be in v4.1
        # We verify by checking the two known issues
        issue_title = issue.get("title", "")
        if issue_title in ["Create automated backup verification system", "Implement container registry garbage collection"]:
            issues_without_security.append(issue)
        # Issues with security label should remain unchanged (in security hardening or wherever)

    if len(issues_without_security) < 2:
        return False, f"Could not find both expected issues without security label. Found: {[i.get('title') for i in issues_without_security]}"

    # Check they are now in the v4.1 Performance milestone
    wrong_milestone = []
    for issue in issues_without_security:
        if issue.get("milestoneId") != performance_ms_id:
            wrong_milestone.append(issue.get("title"))

    if wrong_milestone:
        return False, f"Issues without 'security' label not moved to 'v4.1 - Performance': {wrong_milestone}"

    # Verify that issues WITH the security label that were in Security Hardening remain there
    # Find at least one issue with security label still in the security milestone
    security_label_issues_in_security = []
    for issue in state.get("issues", []):
        if security_label_id in issue.get("labels", []) and issue.get("milestoneId") == security_ms_id:
            security_label_issues_in_security.append(issue)

    if len(security_label_issues_in_security) == 0:
        return False, "All issues were moved out of Security Hardening; issues with 'security' label should remain."

    return True, f"Issues without 'security' label moved to 'v4.1 - Performance'. Issues with 'security' label remain in Security Hardening."
