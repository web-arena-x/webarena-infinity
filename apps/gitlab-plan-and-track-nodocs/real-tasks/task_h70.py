import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # #42 (PostgreSQL upgrade) has highest timeEstimate in v2.1 with 0 timeSpent
    # Should have 16h (57600s) logged and priority::high (12)
    issue = next((i for i in state["issues"] if i["id"] == 42), None)
    if issue is None:
        return False, "Issue #42 not found."
    if issue.get("timeSpent", 0) < 57600:
        return False, f"Issue #42 timeSpent is {issue.get('timeSpent')}, expected at least 57600 (16h)."
    if 12 not in issue.get("labelIds", []):
        return False, f"Issue #42 missing priority::high label (id 12). Labels: {issue.get('labelIds')}."

    return True, "Issue #42: 16h time spent logged, priority set to high."
