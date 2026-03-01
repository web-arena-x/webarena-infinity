import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find the CSP headers issue
    target_issue = None
    for issue in state.get("issues", []):
        if issue.get("title") == "Implement Content Security Policy headers":
            target_issue = issue
            break
    if target_issue is None:
        return False, "Could not find issue 'Implement Content Security Policy headers'."

    issue_id = target_issue["id"]

    # Find a timelog with 3 hours (10800 seconds) and the expected summary
    found_timelog = False
    for tl in state.get("timelogs", []):
        if (tl.get("issueId") == issue_id
                and tl.get("timeSpent") == 10800
                and tl.get("summary") == "Security audit review"):
            found_timelog = True
            break

    if not found_timelog:
        return False, "Could not find a timelog for the CSP issue with 3 hours (10800s) and summary 'Security audit review'."

    return True, "Time entry of 3 hours with summary 'Security audit review' added to the CSP headers issue."
