import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find the issue
    target_issue = None
    for issue in state.get("issues", []):
        if issue.get("title") == "Migrate user settings page to React":
            target_issue = issue
            break
    if target_issue is None:
        return False, "Could not find issue 'Migrate user settings page to React'."

    issue_id = target_issue["id"]
    errors = []

    # Check no timelogs reference this issue
    remaining_timelogs = [t for t in state.get("timelogs", []) if t.get("issueId") == issue_id]
    if remaining_timelogs:
        errors.append(f"Found {len(remaining_timelogs)} remaining time entries (expected 0).")

    # Check time estimate is 20 hours (72000 seconds)
    if target_issue.get("timeEstimate") != 72000:
        errors.append(f"Time estimate is {target_issue.get('timeEstimate')}, expected 72000 (20 hours).")

    if errors:
        return False, " ".join(errors)

    return True, "All time entries deleted from user settings migration issue and time estimate set to 20 hours."
