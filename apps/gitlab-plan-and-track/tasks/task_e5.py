import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issues = state.get("issues", [])

    target_title = "Fix typo in 404 error page message"
    issue = next((i for i in issues if i.get("title") == target_title), None)

    if issue is None:
        return False, f"Could not find issue with title '{target_title}'."

    weight = issue.get("weight")
    if weight != 3:
        return False, f"Issue '{target_title}' weight is {weight!r}, expected 3."

    return True, f"Issue '{target_title}' has weight 3."
