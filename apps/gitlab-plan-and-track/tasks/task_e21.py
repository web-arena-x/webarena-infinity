import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find the issue "Reduce JavaScript bundle size by 40%"
    target_issue = None
    for issue in state.get("issues", []):
        if issue.get("title") == "Reduce JavaScript bundle size by 40%":
            target_issue = issue
            break
    if target_issue is None:
        return False, "Could not find issue 'Reduce JavaScript bundle size by 40%'."

    # Find the todo about this issue
    target_todo = None
    for todo in state.get("todos", []):
        if todo.get("targetId") == target_issue["id"] and todo.get("targetType") == "issue":
            target_todo = todo
            break
    if target_todo is None:
        return False, "Could not find a todo about the JavaScript bundle size issue."

    if target_todo.get("status") != "snoozed":
        return False, f"Todo status is '{target_todo.get('status')}', expected 'snoozed'."

    if target_todo.get("snoozedUntil") is None:
        return False, "Todo has no snoozedUntil date set."

    return True, "Todo about JavaScript bundle size issue is snoozed with a snoozedUntil date."
