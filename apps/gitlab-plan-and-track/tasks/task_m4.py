import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    issues = state.get("issues", [])
    issue = next((i for i in issues if i.get("title") == "Add dark mode support for the entire application"), None)
    if issue is None:
        return False, "Could not find issue titled 'Add dark mode support for the entire application'."

    assignees = issue.get("assignees", [])
    if len(assignees) != 0:
        return False, f"Expected issue to have no assignees but found {len(assignees)} assignee(s)."

    if issue.get("healthStatus") != "needs_attention":
        return False, f"Expected healthStatus 'needs_attention' but got '{issue.get('healthStatus')}'."

    return True, "Issue 'Add dark mode support for the entire application' has no assignees and health status is 'needs_attention'."
