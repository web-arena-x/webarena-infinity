import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issue = next((i for i in state["issues"] if i["title"] == "Login page shows blank screen on Safari 17.2"), None)
    if not issue:
        return False, "Issue 'Login page shows blank screen on Safari 17.2' not found."

    issue_id = issue["id"]

    safari_timelogs = [tl for tl in state["timelogs"] if tl["issueId"] == issue_id and "Safari debugging" in tl.get("summary", "")]
    if safari_timelogs:
        return False, f"Found {len(safari_timelogs)} timelog(s) with 'Safari debugging' in summary for this issue; expected none."

    if issue["timeSpent"] != 0:
        return False, f"Issue timeSpent is {issue['timeSpent']}, expected 0."

    return True, "Issue 'Login page shows blank screen on Safari 17.2' has no 'Safari debugging' timelogs and timeSpent is 0."
