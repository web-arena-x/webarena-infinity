import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issue = next((i for i in state["issues"] if i["title"] == "Implement GraphQL gateway for v3 API"), None)
    if not issue:
        return False, "Issue 'Implement GraphQL gateway for v3 API' not found."

    if issue["healthStatus"] != "at_risk":
        return False, f"Issue healthStatus is '{issue['healthStatus']}', expected 'at_risk'."

    return True, "Issue 'Implement GraphQL gateway for v3 API' has healthStatus set to 'at_risk'."
