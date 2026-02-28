import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issues = state.get("issues", [])

    target_title = "Add webhook support for issue state changes"
    issue = next((i for i in issues if i.get("title") == target_title), None)

    if issue is None:
        return False, f"Could not find issue with title '{target_title}'."

    due_date = issue.get("dueDate")
    if due_date != "2026-04-30":
        return False, f"Issue '{target_title}' dueDate is '{due_date}', expected '2026-04-30'."

    return True, f"Issue '{target_title}' has due date set to 2026-04-30."
