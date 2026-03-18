import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    expected_estimate = 72000  # 20 hours in seconds

    for issue_id in [8, 10, 47, 48]:
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if issue is None:
            return False, f"Issue #{issue_id} not found."
        if issue.get("timeEstimate") != expected_estimate:
            return False, f"Issue #{issue_id} timeEstimate is {issue.get('timeEstimate')}, expected {expected_estimate} (20h)."

    return True, "Issues #8, #10, #47, #48 all have timeEstimate set to 20 hours."
