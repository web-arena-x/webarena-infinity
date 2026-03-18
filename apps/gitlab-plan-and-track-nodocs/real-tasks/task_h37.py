import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    expected_spent = 28800  # 8 hours in seconds

    for issue_id in [19, 21, 53]:
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if issue is None:
            return False, f"Issue #{issue_id} not found."
        if issue.get("timeSpent") != expected_spent:
            return False, f"Issue #{issue_id} timeSpent is {issue.get('timeSpent')}, expected {expected_spent} (8h)."

    return True, "Issues #19, #21, #53 all have 8 hours of time spent logged."
