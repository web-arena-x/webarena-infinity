import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issues = state.get("issues", [])
    todos = state.get("todos", [])

    issue = next((i for i in issues if i["title"] == "Design new navigation header component"), None)
    if not issue:
        return False, "Issue 'Design new navigation header component' not found."

    target = next((t for t in todos if t.get("targetId") == issue["id"] and t.get("action") == "assigned"), None)
    if not target:
        return False, f"No todo found with targetId='{issue['id']}' and action='assigned'."

    if target.get("status") != "pending":
        return False, f"Todo status is '{target.get('status')}', expected 'pending'."

    return True, "Todo for issue 'Design new navigation header component' (action=assigned) has status 'pending'."
