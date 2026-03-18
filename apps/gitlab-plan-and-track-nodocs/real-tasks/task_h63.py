import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # v2.0 (milestoneId 3) open bugs (label 1) with due < 2026-04-01:
    # #28, #35, #78, #101, #104
    # Each should have priority::critical (11) and timeEstimate 72000 (20h)
    target_ids = [28, 35, 78, 101, 104]

    for issue_id in target_ids:
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if issue is None:
            return False, f"Issue #{issue_id} not found."
        if 11 not in issue.get("labelIds", []):
            return False, f"Issue #{issue_id} missing priority::critical (id 11). Labels: {issue.get('labelIds')}."
        if issue.get("timeEstimate") != 72000:
            return False, f"Issue #{issue_id} timeEstimate is {issue.get('timeEstimate')}, expected 72000 (20h)."

    return True, "All v2.0 bugs due before April 1 set to critical with 20h estimate."
