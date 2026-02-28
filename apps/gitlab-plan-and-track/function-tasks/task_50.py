import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issues = state.get("issues", [])
    todos = state.get("todos", [])

    issue = next((i for i in issues if i["title"] == "Email notifications sent with wrong timezone offset"), None)
    if not issue:
        return False, "Issue 'Email notifications sent with wrong timezone offset' not found."

    target = next((t for t in todos if t.get("targetId") == issue["id"] and t.get("action") == "mentioned"), None)
    if not target:
        return False, f"No todo found with targetId='{issue['id']}' and action='mentioned'."

    if target.get("status") != "snoozed":
        return False, f"Todo status is '{target.get('status')}', expected 'snoozed'."

    if target.get("snoozedUntil") is None:
        return False, "Todo snoozedUntil is None, expected a value."

    return True, "Todo for issue 'Email notifications sent with wrong timezone offset' (action=mentioned) is snoozed with snoozedUntil set."
