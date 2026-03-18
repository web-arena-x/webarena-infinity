import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Auth epic children with status::to-do (label 15): #2, #45
    # Both should be closed and removed from epic's childIssueIds
    epic = next((e for e in state["epics"] if "User Authentication" in e.get("title", "")), None)
    if epic is None:
        return False, "User Authentication Overhaul epic not found."

    for issue_id in [2, 45]:
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if issue is None:
            return False, f"Issue #{issue_id} not found."
        if issue.get("status") != "closed":
            return False, f"Issue #{issue_id} status is '{issue.get('status')}', expected 'closed'."
        if issue_id in epic.get("childIssueIds", []):
            return False, f"Issue #{issue_id} still in Auth epic childIssueIds: {epic.get('childIssueIds')}."

    return True, "Auth epic status::to-do children (#2, #45) closed and removed."
