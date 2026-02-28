import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issues = state.get("issues", [])
    users = state.get("users", [])

    target_title = "Upgrade vulnerable dependencies identified in audit"
    issue = next((i for i in issues if i.get("title") == target_title), None)

    if issue is None:
        return False, f"Could not find issue with title '{target_title}'."

    user = next((u for u in users if u.get("name") == "Oliver Schmidt"), None)

    if user is None:
        return False, "Could not find user with name 'Oliver Schmidt'."

    user_id = user.get("id")
    assignees = issue.get("assignees", [])

    if user_id in assignees:
        return False, f"User 'Oliver Schmidt' (id={user_id!r}) is still in the assignees of issue '{target_title}'."

    return True, f"Oliver Schmidt has been unassigned from issue '{target_title}'."
