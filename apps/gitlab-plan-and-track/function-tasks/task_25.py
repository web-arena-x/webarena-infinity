import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issue = next((i for i in state["issues"] if i["title"] == "Dashboard widget layout breaks at 1440px viewport"), None)
    if not issue:
        return False, "Issue 'Dashboard widget layout breaks at 1440px viewport' not found."

    if issue["weight"] is not None:
        return False, f"Issue weight is {issue['weight']}, expected None/null."

    return True, "Issue 'Dashboard widget layout breaks at 1440px viewport' has weight set to null."
