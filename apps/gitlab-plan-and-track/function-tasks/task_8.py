import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issues = state.get("issues", [])

    target = next((i for i in issues if i["title"] == "Login page shows blank screen on Safari 17.2"), None)
    if not target:
        return False, "Issue 'Login page shows blank screen on Safari 17.2' not found."

    assignees = target.get("assignees", [])
    if "usr_7" not in assignees:
        return False, f"'usr_7' (Nina Kowalski) not in assignees: {assignees}."
    if "usr_8" not in assignees:
        return False, f"'usr_8' (David Kim) not in assignees: {assignees}."

    return True, "Issue 'Login page shows blank screen on Safari 17.2' has both usr_7 (Nina Kowalski) and usr_8 (David Kim) as assignees."
