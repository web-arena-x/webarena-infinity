import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issue = next((i for i in state["issues"] if i["title"] == "Fix dropdown menu position clipping at viewport edges"), None)
    if not issue:
        return False, "Issue 'Fix dropdown menu position clipping at viewport edges' not found."

    if issue["timeEstimate"] != 14400:
        return False, f"Issue timeEstimate is {issue['timeEstimate']}, expected 14400."

    return True, "Issue 'Fix dropdown menu position clipping at viewport edges' has timeEstimate set to 14400."
