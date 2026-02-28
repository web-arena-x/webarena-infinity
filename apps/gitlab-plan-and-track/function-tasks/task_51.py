import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issues = state.get("issues", [])
    todos = state.get("todos", [])

    issue = next((i for i in issues if i["title"] == "Implement GraphQL gateway for v3 API"), None)
    if not issue:
        return False, "Issue 'Implement GraphQL gateway for v3 API' not found."

    target = next((t for t in todos if t.get("targetId") == issue["id"] and t.get("action") == "review_requested"), None)
    if not target:
        return False, f"No todo found with targetId='{issue['id']}' and action='review_requested'."

    if target.get("status") != "pending":
        return False, f"Todo status is '{target.get('status')}', expected 'pending'."

    if target.get("snoozedUntil") is not None:
        return False, f"Todo snoozedUntil is '{target.get('snoozedUntil')}', expected None."

    return True, "Todo for issue 'Implement GraphQL gateway for v3 API' (action=review_requested) is pending with snoozedUntil=None."
