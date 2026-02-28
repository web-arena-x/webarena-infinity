import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issues = state.get("issues", [])

    target_title = "Markdown preview renders incorrectly with nested code blocks"
    issue = next((i for i in issues if i.get("title") == target_title), None)

    if issue is not None:
        return False, f"Issue with title '{target_title}' still exists but should have been deleted."

    return True, f"Issue '{target_title}' has been deleted."
