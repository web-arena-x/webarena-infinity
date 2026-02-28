import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issues = state.get("issues", [])

    target_title = "Reduce JavaScript bundle size by 40%"
    issue = next((i for i in issues if i.get("title") == target_title), None)

    if issue is None:
        return False, f"Could not find issue with title '{target_title}'."

    health_status = issue.get("healthStatus")
    if health_status != "at_risk":
        return False, f"Issue '{target_title}' healthStatus is '{health_status}', expected 'at_risk'."

    return True, f"Issue '{target_title}' health status is 'at_risk'."
