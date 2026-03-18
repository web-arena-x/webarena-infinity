import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Backlog milestone should be closed
    backlog = next((m for m in state["milestones"] if m["title"] == "Backlog"), None)
    if backlog is None:
        return False, "Backlog milestone not found."
    if backlog.get("status") != "closed":
        return False, f"Backlog milestone status is '{backlog.get('status')}', expected 'closed'."

    # Issues #68, #105, #112 should be in v2.1 Integrations (milestoneId 4)
    for issue_id in [68, 105, 112]:
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if issue is None:
            return False, f"Issue #{issue_id} not found."
        if issue.get("milestoneId") != 4:
            return False, f"Issue #{issue_id} milestoneId is {issue.get('milestoneId')}, expected 4 (v2.1 Integrations)."

    return True, "Backlog milestone closed; feature+backend issues #68, #105, #112 moved to v2.1."
