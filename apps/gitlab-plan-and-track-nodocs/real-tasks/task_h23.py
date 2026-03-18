import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Check label exists
    label = next((l for l in state["labels"] if l["name"] == "sprint-blocker"), None)
    if label is None:
        return False, "Label 'sprint-blocker' not found."

    if label.get("color") != "#e74c3c":
        return False, f"Label 'sprint-blocker' color is '{label.get('color')}', expected '#e74c3c'."

    label_id = label["id"]

    # Find current engineering sprint
    eng_sprints = [it for it in state["iterations"] if it.get("status") == "current" and it.get("cadenceId") == 1]
    if not eng_sprints:
        return False, "No current engineering sprint found."
    current_sprint_id = eng_sprints[0]["id"]

    # Find priority::critical label
    critical_label = next((l for l in state["labels"] if l["name"] == "priority::critical"), None)
    if critical_label is None:
        return False, "Label 'priority::critical' not found."
    critical_id = critical_label["id"]

    # Check all open critical issues in current sprint have the new label
    target_issues = [
        i for i in state["issues"]
        if i["status"] == "open"
        and i.get("iterationId") == current_sprint_id
        and critical_id in i.get("labelIds", [])
    ]

    if not target_issues:
        return False, "No open critical-priority issues found in current sprint."

    for issue in target_issues:
        if label_id not in issue.get("labelIds", []):
            return False, f"Issue #{issue['id']} missing 'sprint-blocker' label."

    return True, f"Label 'sprint-blocker' created and applied to {len(target_issues)} critical issues in current sprint."
