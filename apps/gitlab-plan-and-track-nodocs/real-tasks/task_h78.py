import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # v2.1 (milestoneId 4) unassigned open issues with feature (2) + medium (13):
    # #62, #64, #74, #80, #111, #126
    # Each should have weight 3 and Priya (5) in assigneeIds
    target_ids = [62, 64, 74, 80, 111, 126]

    for issue_id in target_ids:
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if issue is None:
            return False, f"Issue #{issue_id} not found."
        if issue.get("weight") != 3:
            return False, f"Issue #{issue_id} weight is {issue.get('weight')}, expected 3."
        if 5 not in issue.get("assigneeIds", []):
            return False, f"Priya Sharma (id 5) not in assigneeIds for issue #{issue_id}: {issue.get('assigneeIds')}."

    return True, "6 unassigned v2.1 feature/medium issues: weight 3, assigned to Priya."
