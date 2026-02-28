import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issue = next((i for i in state["issues"] if i["title"] == "Implement retry mechanism for failed API calls"), None)
    if not issue:
        return False, "Issue 'Implement retry mechanism for failed API calls' not found."

    issue_id = issue["id"]

    timelog = next((tl for tl in state["timelogs"] if tl["issueId"] == issue_id and tl["timeSpent"] == 9000), None)
    if not timelog:
        return False, f"No timelog found for issue '{issue_id}' with timeSpent == 9000."

    if issue["timeSpent"] < 9000:
        return False, f"Issue timeSpent is {issue['timeSpent']}, expected >= 9000."

    return True, "Issue 'Implement retry mechanism for failed API calls' has a timelog with timeSpent 9000 and issue timeSpent >= 9000."
