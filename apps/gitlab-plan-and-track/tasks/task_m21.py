import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # The open issue with the highest weight is "Build real-time collaborative editing
    # for issue descriptions" (weight 21)
    target_issue = None
    for issue in state.get("issues", []):
        if issue.get("title") == "Build real-time collaborative editing for issue descriptions":
            target_issue = issue
            break
    if target_issue is None:
        return False, "Could not find issue 'Build real-time collaborative editing for issue descriptions'."

    if target_issue.get("healthStatus") != "at_risk":
        return False, f"Issue health status is '{target_issue.get('healthStatus')}', expected 'at_risk'."

    return True, "The highest-weight open issue has its health status set to 'at risk'."
