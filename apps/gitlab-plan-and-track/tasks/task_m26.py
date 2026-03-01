import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find the file upload bug
    target_issue = None
    for issue in state.get("issues", []):
        if issue.get("title") == "File upload fails silently for files > 50MB":
            target_issue = issue
            break
    if target_issue is None:
        return False, "Could not find issue 'File upload fails silently for files > 50MB'."

    # Check time estimate is 1 day (28800 seconds)
    if target_issue.get("timeEstimate") != 28800:
        return False, f"Time estimate is {target_issue.get('timeEstimate')}, expected 28800 (1 day)."

    # Check for a timelog with 2 hours and correct summary
    issue_id = target_issue["id"]
    found_timelog = False
    for tl in state.get("timelogs", []):
        if (tl.get("issueId") == issue_id
                and tl.get("timeSpent") == 7200
                and tl.get("summary") == "Reproducing the issue"):
            found_timelog = True
            break

    if not found_timelog:
        return False, "Could not find a timelog with 2 hours (7200s) and summary 'Reproducing the issue'."

    return True, "File upload bug has 1-day time estimate and 2-hour timelog with correct summary."
