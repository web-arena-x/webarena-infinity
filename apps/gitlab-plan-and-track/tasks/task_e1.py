import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issues = state.get("issues", [])

    target_title = "Login page shows blank screen on Safari 17.2"
    issue = next((i for i in issues if i.get("title") == target_title), None)

    if issue is None:
        return False, f"Could not find issue with title '{target_title}'."

    if issue.get("status") != "closed":
        return False, f"Issue '{target_title}' status is '{issue.get('status')}', expected 'closed'."

    if issue.get("closedAt") is None:
        return False, f"Issue '{target_title}' has no closedAt date set."

    return True, f"Issue '{target_title}' is closed with a closedAt date."
