import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issues = state.get("issues", [])
    todos = state.get("todos", [])

    issue = next((i for i in issues if i["title"] == "Login page shows blank screen on Safari 17.2"), None)
    if not issue:
        return False, "Issue 'Login page shows blank screen on Safari 17.2' not found."

    target = next((t for t in todos if t.get("targetId") == issue["id"] and t.get("action") == "assigned"), None)
    if not target:
        return False, f"No todo found with targetId='{issue['id']}' and action='assigned'."

    if target.get("status") != "done":
        return False, f"Todo status is '{target.get('status')}', expected 'done'."

    return True, "Todo for issue 'Login page shows blank screen on Safari 17.2' (action=assigned) has status 'done'."
