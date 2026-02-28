import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issues = state.get("issues", [])

    target_title = "Add rate limiting to v3 endpoints"
    issue = next((i for i in issues if i.get("title") == target_title), None)

    if issue is None:
        return False, f"Could not find issue with title '{target_title}'."

    if not issue.get("confidential"):
        return False, f"Issue '{target_title}' is not marked confidential."

    return True, f"Issue '{target_title}' is marked as confidential."
