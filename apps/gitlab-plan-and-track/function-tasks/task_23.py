import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issue = next((i for i in state["issues"] if i["title"] == "Email notifications sent with wrong timezone offset"), None)
    if not issue:
        return False, "Issue 'Email notifications sent with wrong timezone offset' not found."

    if issue["dueDate"] is not None:
        return False, f"Issue dueDate is '{issue['dueDate']}', expected None/null."

    return True, "Issue 'Email notifications sent with wrong timezone offset' has dueDate set to null."
