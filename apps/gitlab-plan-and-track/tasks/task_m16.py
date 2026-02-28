import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    issues = state.get("issues", [])
    issue = next((i for i in issues if i.get("title") == "Build component library documentation site"), None)
    if issue is None:
        return False, "Could not find issue titled 'Build component library documentation site'."

    users = state.get("users", [])
    priya = next((u for u in users if u.get("name") == "Priya Patel"), None)
    if priya is None:
        return False, "Could not find user named 'Priya Patel'."

    marcus = next((u for u in users if u.get("name") == "Marcus Johnson"), None)
    if marcus is None:
        return False, "Could not find user named 'Marcus Johnson'."

    issue_assignees = issue.get("assignees", [])

    if priya.get("id") not in issue_assignees:
        return False, f"User 'Priya Patel' (id: {priya.get('id')}) is not in issue's assignees."

    if marcus.get("id") not in issue_assignees:
        return False, f"User 'Marcus Johnson' (id: {marcus.get('id')}) is not in issue's assignees."

    return True, "Both Priya Patel and Marcus Johnson are assigned to the 'Build component library documentation site' issue."
