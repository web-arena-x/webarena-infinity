import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issue = next((i for i in state["issues"] if i["title"] == "Upgrade vulnerable dependencies identified in audit"), None)
    if not issue:
        return False, "Issue 'Upgrade vulnerable dependencies identified in audit' not found."

    if issue["healthStatus"] is not None:
        return False, f"Issue healthStatus is '{issue['healthStatus']}', expected None/null."

    return True, "Issue 'Upgrade vulnerable dependencies identified in audit' has healthStatus set to null."
