import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    david_id = next((u["id"] for u in state["users"] if "David Kim" in u.get("name", "")), None)
    if david_id is None:
        return False, "User 'David Kim' not found."

    for issue_id in [7, 47]:
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if issue is None:
            return False, f"Issue #{issue_id} not found."
        if david_id not in issue.get("assigneeIds", []):
            return False, f"David Kim (id {david_id}) not in assigneeIds for issue #{issue_id}: {issue.get('assigneeIds')}."

    return True, "David Kim assigned to issues #7 and #47."
