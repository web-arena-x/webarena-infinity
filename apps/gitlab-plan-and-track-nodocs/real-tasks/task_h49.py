import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Backlog milestone description updated
    backlog = next((m for m in state["milestones"] if m["title"] == "Backlog"), None)
    if backlog is None:
        return False, "Backlog milestone not found."
    expected_desc = "Deferred work — not scheduled for active development"
    if backlog.get("description") != expected_desc:
        return False, f"Backlog description is '{backlog.get('description')}', expected '{expected_desc}'."

    # Issues with weight <= 1 in Backlog should be closed: #72, #120, #127, #129
    for issue_id in [72, 120, 127, 129]:
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if issue is None:
            return False, f"Issue #{issue_id} not found."
        if issue["status"] != "closed":
            return False, f"Issue #{issue_id} status is '{issue['status']}', expected 'closed'."

    return True, "Backlog description updated; issues #72, #120, #127, #129 (weight ≤ 1) closed."
