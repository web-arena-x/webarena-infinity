import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Milestone 'Emergency Fixes' must exist with dueDate 2026-04-15
    ms = next((m for m in state["milestones"] if m["title"] == "Emergency Fixes"), None)
    if ms is None:
        return False, "Milestone 'Emergency Fixes' not found."
    if ms.get("dueDate") != "2026-04-15":
        return False, f"Milestone 'Emergency Fixes' dueDate is '{ms.get('dueDate')}', expected '2026-04-15'."

    ms_id = ms["id"]

    # Issues #11, #33, #41 must be in the new milestone
    for issue_id in [11, 33, 41]:
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if issue is None:
            return False, f"Issue #{issue_id} not found."
        if issue["milestoneId"] != ms_id:
            return False, f"Issue #{issue_id} milestoneId is {issue['milestoneId']}, expected {ms_id} (Emergency Fixes)."

    return True, "Milestone 'Emergency Fixes' created and critical Sprint 6 issues (#11, #33, #41) moved into it."
