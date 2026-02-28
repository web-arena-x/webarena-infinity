import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issue = next((i for i in state["issues"] if i["title"] == "Add webhook support for issue state changes"), None)
    if not issue:
        return False, "Issue 'Add webhook support for issue state changes' not found."

    if issue["weight"] != 13:
        return False, f"Issue weight is {issue['weight']}, expected 13."

    return True, "Issue 'Add webhook support for issue state changes' has weight set to 13."
