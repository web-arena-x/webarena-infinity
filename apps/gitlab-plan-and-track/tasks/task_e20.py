import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issues = state.get("issues", [])
    todos = state.get("todos", [])

    target_title = "Implement GraphQL gateway for v3 API"
    issue = next((i for i in issues if i.get("title") == target_title), None)

    if issue is None:
        return False, f"Could not find issue with title '{target_title}'."

    issue_id = issue.get("id")
    todo = next(
        (t for t in todos if t.get("targetId") == issue_id and t.get("action") == "review_requested"),
        None,
    )

    if todo is None:
        return False, f"Could not find a todo with action 'review_requested' for issue '{target_title}'."

    if todo.get("status") != "pending":
        return False, (
            f"Todo for issue '{target_title}' status is '{todo.get('status')}', "
            f"expected 'pending' (restored from snoozed)."
        )

    if todo.get("snoozedUntil") is not None:
        return False, (
            f"Todo for issue '{target_title}' still has snoozedUntil set to '{todo.get('snoozedUntil')}', "
            f"expected None."
        )

    return True, f"Todo for issue '{target_title}' has been restored from snoozed (status=pending, snoozedUntil=None)."
