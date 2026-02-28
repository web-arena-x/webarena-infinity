import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issue = next((i for i in state["issues"] if i["title"] == "Analyze and optimize slow queries from APM logs"), None)
    if not issue:
        return False, "Issue 'Analyze and optimize slow queries from APM logs' not found."

    if issue["iterationId"] is not None:
        return False, f"Issue iterationId is '{issue['iterationId']}', expected None/null."

    return True, "Issue 'Analyze and optimize slow queries from APM logs' has iterationId set to null."
