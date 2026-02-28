import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Check that NO todo has status == "pending"
    pending_todos = []
    for todo in state.get("todos", []):
        if todo.get("status") == "pending":
            pending_todos.append(todo.get("id", "unknown"))

    if pending_todos:
        return False, f"There are still {len(pending_todos)} pending todo(s): {pending_todos}"

    # Find issue "Review Q1 objectives"
    target_issue = None
    for issue in state.get("issues", []):
        if issue.get("title") == "Review Q1 objectives":
            target_issue = issue
            break
    if target_issue is None:
        return False, "Could not find issue 'Review Q1 objectives'."

    # Find label "priority::medium"
    medium_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "priority::medium":
            medium_label = lbl
            break
    if medium_label is None:
        return False, "Could not find label 'priority::medium'."
    medium_label_id = medium_label["id"]

    # The current user is usr_1 (Sarah Chen) - find by checking current user or by name
    current_user_id = None
    current_user = state.get("currentUser")
    if current_user:
        current_user_id = current_user if isinstance(current_user, str) else current_user.get("id")
    if current_user_id is None:
        # Fall back to finding Sarah Chen
        for user in state.get("users", []):
            if user.get("name") == "Sarah Chen":
                current_user_id = user["id"]
                break

    if current_user_id is None:
        return False, "Could not determine current user (Sarah Chen / usr_1)."

    # Check issue is open
    if target_issue.get("status") != "open":
        return False, f"Issue 'Review Q1 objectives' has status='{target_issue.get('status')}', expected 'open'."

    # Check current user is in assignees
    assignees = target_issue.get("assignees", [])
    if current_user_id not in assignees:
        return False, f"Current user '{current_user_id}' is not assigned to 'Review Q1 objectives'."

    # Check priority::medium label is applied
    if medium_label_id not in target_issue.get("labels", []):
        return False, "Label 'priority::medium' is not applied to 'Review Q1 objectives'."

    return True, "All pending todos marked as done, and issue 'Review Q1 objectives' created with correct attributes."
