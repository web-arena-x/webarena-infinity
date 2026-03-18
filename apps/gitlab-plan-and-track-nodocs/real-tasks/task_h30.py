import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    todo_label = next((l for l in state["labels"] if l["name"] == "status::to-do"), None)
    ip_label = next((l for l in state["labels"] if l["name"] == "status::in-progress"), None)
    high_label = next((l for l in state["labels"] if l["name"] == "priority::high"), None)
    if not todo_label or not ip_label or not high_label:
        return False, "Required labels not found."

    todo_id = todo_label["id"]
    ip_id = ip_label["id"]

    # Issues #2 and #23 should have in-progress, not to-do
    for issue_id in [2, 23]:
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if issue is None:
            return False, f"Issue #{issue_id} not found."
        if todo_id in issue.get("labelIds", []):
            return False, f"Issue #{issue_id} still has status::to-do label."
        if ip_id not in issue.get("labelIds", []):
            return False, f"Issue #{issue_id} does not have status::in-progress label."

    return True, "Issues #2 and #23 changed from to-do to in-progress."
