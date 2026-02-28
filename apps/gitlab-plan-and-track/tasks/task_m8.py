import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    users = state.get("users", [])
    user = next((u for u in users if u.get("name") == "Fatima Al-Rashid"), None)
    if user is None:
        return False, "Could not find user named 'Fatima Al-Rashid'."

    user_id = user.get("id")
    issues = state.get("issues", [])
    assigned_issues = [i for i in issues if user_id in i.get("assignees", [])]

    if len(assigned_issues) == 0:
        return False, "No issues found assigned to 'Fatima Al-Rashid'."

    open_issues = [i for i in assigned_issues if i.get("status") != "closed"]
    if len(open_issues) > 0:
        open_titles = [i.get("title") for i in open_issues]
        return False, f"Found {len(open_issues)} open issue(s) still assigned to 'Fatima Al-Rashid': {open_titles}."

    return True, f"All {len(assigned_issues)} issue(s) assigned to 'Fatima Al-Rashid' are now closed."
