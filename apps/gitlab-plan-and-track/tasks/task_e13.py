import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issues = state.get("issues", [])
    users = state.get("users", [])

    target_title = "Add dark mode support for the entire application"
    issue = next((i for i in issues if i.get("title") == target_title), None)

    if issue is None:
        return False, f"Could not find issue with title '{target_title}'."

    user = next((u for u in users if u.get("name") == "Nina Kowalski"), None)

    if user is None:
        return False, "Could not find user with name 'Nina Kowalski'."

    user_id = user.get("id")
    assignees = issue.get("assignees", [])

    if user_id in assignees:
        return False, f"User 'Nina Kowalski' (id={user_id!r}) is still in the assignees of issue '{target_title}'."

    return True, f"Nina Kowalski has been removed from the assignees of issue '{target_title}'."
