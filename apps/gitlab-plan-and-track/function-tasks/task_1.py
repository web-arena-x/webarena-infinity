import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issues = state.get("issues", [])

    target = next((i for i in issues if i["title"] == "Implement user profile badges"), None)
    if not target:
        return False, "Issue with title 'Implement user profile badges' not found."

    if target.get("weight") != 5:
        return False, f"Issue weight is {target.get('weight')}, expected 5."

    if target.get("status") != "open":
        return False, f"Issue status is '{target.get('status')}', expected 'open'."

    return True, "Issue 'Implement user profile badges' exists with weight 5 and status 'open'."
