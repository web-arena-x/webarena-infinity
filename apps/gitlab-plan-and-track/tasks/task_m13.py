import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    issues = state.get("issues", [])
    issue = next((i for i in issues if i.get("title") == "Implement retry mechanism for failed API calls"), None)
    if issue is None:
        return False, "Could not find issue titled 'Implement retry mechanism for failed API calls'."

    if issue.get("startDate") != "2026-03-15":
        return False, f"Expected startDate '2026-03-15' but got '{issue.get('startDate')}'."

    if issue.get("dueDate") != "2026-04-15":
        return False, f"Expected dueDate '2026-04-15' but got '{issue.get('dueDate')}'."

    return True, "Issue 'Implement retry mechanism for failed API calls' has correct start date (2026-03-15) and due date (2026-04-15)."
