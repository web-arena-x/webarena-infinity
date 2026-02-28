import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issue = next((i for i in state["issues"] if i["title"] == "Update project README with new setup instructions"), None)
    if not issue:
        return False, "Issue 'Update project README with new setup instructions' not found."

    if issue["milestoneId"] is not None:
        return False, f"Issue milestoneId is '{issue['milestoneId']}', expected None/null."

    return True, "Issue 'Update project README with new setup instructions' has milestoneId set to null."
