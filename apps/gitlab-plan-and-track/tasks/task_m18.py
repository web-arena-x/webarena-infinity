import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    issues = state.get("issues", [])
    issue = next((i for i in issues if i.get("title") == "Migrate user authentication from sessions to JWT"), None)
    if issue is None:
        return False, "Could not find issue titled 'Migrate user authentication from sessions to JWT'."

    labels = state.get("labels", [])
    label = next((l for l in labels if l.get("title") == "performance"), None)
    if label is None:
        return False, "Could not find label titled 'performance'."

    if label.get("id") not in issue.get("labels", []):
        return False, f"Label 'performance' (id: {label.get('id')}) is not in issue's labels."

    if issue.get("healthStatus") != "needs_attention":
        return False, f"Expected healthStatus 'needs_attention' but got '{issue.get('healthStatus')}'."

    return True, "Issue 'Migrate user authentication from sessions to JWT' has 'performance' label and health status 'needs_attention'."
