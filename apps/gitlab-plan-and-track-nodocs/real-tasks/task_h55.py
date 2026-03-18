import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Tom Ramirez (id 6) v2.1 issues: #19, #20, #21, #42, #50, #53
    # Each should have 8h (28800s) time spent logged
    for issue_id in [19, 20, 21, 42, 50, 53]:
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if issue is None:
            return False, f"Issue #{issue_id} not found."
        if issue.get("timeSpent", 0) < 28800:
            return False, f"Issue #{issue_id} timeSpent is {issue.get('timeSpent')}, expected at least 28800 (8h)."

    return True, "8 hours of time spent logged on each of Tom's 6 v2.1 issues."
