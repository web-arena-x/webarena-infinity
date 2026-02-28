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
    aisha = next((u for u in users if u.get("name") == "Aisha Mohammed"), None)
    if aisha is None:
        return False, "Could not find user named 'Aisha Mohammed'."

    nina = next((u for u in users if u.get("name") == "Nina Kowalski"), None)
    if nina is None:
        return False, "Could not find user named 'Nina Kowalski'."

    issue_assignees = issue.get("assignees", [])

    if aisha.get("id") in issue_assignees:
        return False, f"User 'Aisha Mohammed' (id: {aisha.get('id')}) should have been removed from issue's assignees but is still present."

    if nina.get("id") not in issue_assignees:
        return False, f"User 'Nina Kowalski' (id: {nina.get('id')}) should have been added to issue's assignees but is not present."

    return True, "Aisha Mohammed removed and Nina Kowalski added as assignee on 'Build component library documentation site' issue."
