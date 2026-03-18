import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Issues with devops+tech-debt: #42 and #54
    for issue_id in [42, 54]:
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if issue is None:
            return False, f"Issue #{issue_id} not found."
        # tech-debt (10) should be removed
        if 10 in issue.get("labelIds", []):
            return False, f"Issue #{issue_id} still has tech-debt label (id 10). Labels: {issue.get('labelIds')}."
        # performance (4) should be added
        if 4 not in issue.get("labelIds", []):
            return False, f"Issue #{issue_id} missing performance label (id 4). Labels: {issue.get('labelIds')}."
        # weight should be 8
        if issue.get("weight") != 8:
            return False, f"Issue #{issue_id} weight is {issue.get('weight')}, expected 8."

    return True, "Issues #42 and #54: tech-debt replaced with performance, weight set to 8."
