import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Epic 'API v3 Migration' should be closed
    epic = next((e for e in state["epics"] if "API v3 Migration" in e.get("title", "")), None)
    if epic is None:
        return False, "API v3 Migration epic not found."
    if epic.get("status") != "closed":
        return False, f"API v3 Migration epic status is '{epic.get('status')}', expected 'closed'."

    # All open children should be closed: #7, #8, #9, #10, #47, #48
    for issue_id in [7, 8, 9, 10, 47, 48]:
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if issue is None:
            return False, f"Issue #{issue_id} not found."
        if issue["status"] != "closed":
            return False, f"Issue #{issue_id} status is '{issue['status']}', expected 'closed'."

    # breaking-change (20) should be removed from #7, #8, #10, #47
    for issue_id in [7, 8, 10, 47]:
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if 20 in issue.get("labelIds", []):
            return False, f"Issue #{issue_id} still has breaking-change label (id 20). Labels: {issue.get('labelIds')}."

    return True, "API v3 Migration epic closed, all children closed, breaking-change labels removed."
