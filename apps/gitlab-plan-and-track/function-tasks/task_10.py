import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issues = state.get("issues", [])

    target = next((i for i in issues if i["title"] == "Implement CSRF token rotation"), None)
    if not target:
        return False, "Issue 'Implement CSRF token rotation' not found."

    assignees = target.get("assignees", [])
    if "usr_10" not in assignees:
        return False, f"'usr_10' (Chen Wei) not in assignees: {assignees}."

    return True, "Issue 'Implement CSRF token rotation' has usr_10 (Chen Wei) as an assignee."
