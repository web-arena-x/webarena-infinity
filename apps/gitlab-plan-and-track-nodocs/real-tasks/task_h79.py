import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Two open issues with devops (9) + tech-debt (10): #42, #54
    # Both should be closed and have priority::high (12)
    for issue_id in [42, 54]:
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if issue is None:
            return False, f"Issue #{issue_id} not found."
        if issue.get("status") != "closed":
            return False, f"Issue #{issue_id} status is '{issue.get('status')}', expected 'closed'."
        if 12 not in issue.get("labelIds", []):
            return False, f"Issue #{issue_id} missing priority::high (id 12). Labels: {issue.get('labelIds')}."

    return True, "Both devops+tech-debt issues (#42, #54) closed with priority::high."
