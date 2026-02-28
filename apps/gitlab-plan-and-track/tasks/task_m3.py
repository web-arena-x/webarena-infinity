import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    issues = state.get("issues", [])
    issue = next((i for i in issues if i.get("title") == "Set up monitoring dashboard"), None)
    if issue is None:
        return False, "Could not find issue titled 'Set up monitoring dashboard'."

    users = state.get("users", [])
    user = next((u for u in users if u.get("name") == "Luca Rossi"), None)
    if user is None:
        return False, "Could not find user named 'Luca Rossi'."

    labels = state.get("labels", [])
    label = next((l for l in labels if l.get("title") == "priority::high"), None)
    if label is None:
        return False, "Could not find label titled 'priority::high'."

    if user.get("id") not in issue.get("assignees", []):
        return False, f"User 'Luca Rossi' (id: {user.get('id')}) is not in issue's assignees."

    if label.get("id") not in issue.get("labels", []):
        return False, f"Label 'priority::high' (id: {label.get('id')}) is not in issue's labels."

    if issue.get("status") != "open":
        return False, f"Expected issue status 'open' but got '{issue.get('status')}'."

    return True, "Issue 'Set up monitoring dashboard' created and correctly assigned to Luca Rossi with priority::high label."
