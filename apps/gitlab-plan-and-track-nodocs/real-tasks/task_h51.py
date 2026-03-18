import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Emily's open bugs with no iteration: #37, #67, #72, #110, #120
    # Each should have iterationId 13 (Design Cycle 5) and priority::medium (13)
    expected_issues = [37, 67, 72, 110, 120]
    for issue_id in expected_issues:
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if issue is None:
            return False, f"Issue #{issue_id} not found."
        if issue.get("iterationId") != 13:
            return False, f"Issue #{issue_id} iterationId is {issue.get('iterationId')}, expected 13 (Design Cycle 5)."
        if 13 not in issue.get("labelIds", []):
            return False, f"Issue #{issue_id} does not have priority::medium (id 13). Labels: {issue.get('labelIds')}."

    return True, "Emily's 5 unscheduled bugs set to Design Cycle 5 with priority::medium."
