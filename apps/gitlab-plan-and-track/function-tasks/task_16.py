import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issue = next((i for i in state["issues"] if i["title"] == "Dashboard widget layout breaks at 1440px viewport"), None)
    if not issue:
        return False, "Issue 'Dashboard widget layout breaks at 1440px viewport' not found."

    iteration = next((it for it in state["iterations"] if it["title"] == "Sprint 27"), None)
    if not iteration:
        return False, "Iteration 'Sprint 27' not found."

    if issue["iterationId"] != iteration["id"]:
        return False, f"Issue iterationId is '{issue['iterationId']}', expected '{iteration['id']}'."

    return True, "Issue 'Dashboard widget layout breaks at 1440px viewport' has iterationId matching 'Sprint 27'."
