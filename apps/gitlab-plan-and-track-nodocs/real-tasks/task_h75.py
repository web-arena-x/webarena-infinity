import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Emily (8) open issues in v2.0 (milestoneId 3): #22, #23, #31, #78
    # Each should have priority::high (12) and dueDate 2026-04-15
    target_ids = [22, 23, 31, 78]

    for issue_id in target_ids:
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if issue is None:
            return False, f"Issue #{issue_id} not found."
        if 12 not in issue.get("labelIds", []):
            return False, f"Issue #{issue_id} missing priority::high (id 12). Labels: {issue.get('labelIds')}."
        if issue.get("dueDate") != "2026-04-15":
            return False, f"Issue #{issue_id} dueDate is '{issue.get('dueDate')}', expected '2026-04-15'."

    return True, "Emily's v2.0 issues set to priority::high with due date 2026-04-15."
