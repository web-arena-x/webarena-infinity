import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issue = next((i for i in state["issues"] if i["title"] == "Build component library documentation site"), None)
    if not issue:
        return False, "Issue 'Build component library documentation site' not found."

    if issue["epicId"] is not None:
        return False, f"Issue epicId is '{issue['epicId']}', expected None/null."

    return True, "Issue 'Build component library documentation site' has epicId set to null."
