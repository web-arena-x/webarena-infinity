import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issues = state.get("issues", [])

    target = next((i for i in issues if i["title"] == "Migrate user settings page to React"), None)
    if not target:
        return False, "Issue 'Migrate user settings page to React' not found."

    assignees = target.get("assignees", [])
    if "usr_7" not in assignees:
        return False, f"'usr_7' (Nina Kowalski) not in assignees: {assignees}. She should still be assigned."

    if "usr_11" in assignees:
        return False, f"'usr_11' (Alex Thompson) is still in assignees: {assignees}. Expected usr_11 to be removed."

    return True, "Issue 'Migrate user settings page to React' has usr_7 (Nina Kowalski) in assignees and usr_11 (Alex Thompson) removed."
