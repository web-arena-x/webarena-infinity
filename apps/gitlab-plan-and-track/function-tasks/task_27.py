import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issue = next((i for i in state["issues"] if i["title"] == "Implement lazy loading for images and avatars"), None)
    if not issue:
        return False, "Issue 'Implement lazy loading for images and avatars' not found."

    if issue["timeEstimate"] != 0:
        return False, f"Issue timeEstimate is {issue['timeEstimate']}, expected 0."

    return True, "Issue 'Implement lazy loading for images and avatars' has timeEstimate set to 0."
