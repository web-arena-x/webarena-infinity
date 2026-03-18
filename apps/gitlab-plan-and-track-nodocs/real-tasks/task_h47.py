import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # #11, #12, #49 must be closed with 8h additional time spent
    expected = {
        11: 21600 + 28800,  # 50400
        12: 0 + 28800,      # 28800
        49: 0 + 28800,      # 28800
    }

    for issue_id, expected_time in expected.items():
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if issue is None:
            return False, f"Issue #{issue_id} not found."
        if issue["status"] != "closed":
            return False, f"Issue #{issue_id} status is '{issue['status']}', expected 'closed'."
        if issue.get("timeSpent", 0) < expected_time:
            return False, f"Issue #{issue_id} timeSpent is {issue.get('timeSpent')}, expected at least {expected_time}."

    return True, "Issues #11, #12, #49 closed with 8 hours time spent logged on each."
