import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find Oliver Schmidt
    oliver = None
    for u in state.get("users", []):
        if u.get("name") == "Oliver Schmidt":
            oliver = u
            break
    if oliver is None:
        return False, "Could not find user 'Oliver Schmidt'."

    oliver_id = oliver["id"]

    # Expected issues assigned to Oliver Schmidt (open in seed)
    expected_titles = [
        "Implement Content Security Policy headers",
        "Upgrade vulnerable dependencies identified in audit",
        "Implement two-factor authentication with TOTP",
    ]

    errors = []
    for title in expected_titles:
        issue = None
        for i in state.get("issues", []):
            if i.get("title") == title:
                issue = i
                break
        if issue is None:
            errors.append(f"Could not find issue '{title}'.")
            continue

        # Check health status
        if issue.get("healthStatus") != "on_track":
            errors.append(f"Issue '{title}' health is '{issue.get('healthStatus')}', expected 'on_track'.")

        # Check timelog exists with correct summary
        issue_id = issue["id"]
        matching_logs = [t for t in state.get("timelogs", [])
                         if t.get("issueId") == issue_id
                         and t.get("summary") == "Sprint planning review"
                         and t.get("timeSpent") == 3600]
        if not matching_logs:
            errors.append(f"Issue '{title}' missing 1-hour timelog with summary 'Sprint planning review'.")

    if errors:
        return False, " ".join(errors)

    return True, f"Time logged and health set to 'on track' for all {len(expected_titles)} of Oliver Schmidt's issues."
