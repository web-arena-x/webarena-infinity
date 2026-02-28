import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issues = state.get("issues", [])

    target = next((i for i in issues if i["title"] == "Markdown preview renders incorrectly with nested code blocks"), None)
    if target is not None:
        return False, "Issue 'Markdown preview renders incorrectly with nested code blocks' still exists (expected it to be deleted)."

    return True, "Issue 'Markdown preview renders incorrectly with nested code blocks' has been deleted."
