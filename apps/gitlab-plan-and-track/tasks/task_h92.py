import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # Find the user settings migration issue
    issue = None
    for i in state.get("issues", []):
        if i.get("title") == "Migrate user settings page to React":
            issue = i
            break
    if issue is None:
        return False, "Could not find issue 'Migrate user settings page to React'."

    # Check timelog
    found_timelog = False
    for tl in state.get("timelogs", []):
        if (
            tl.get("issueId") == issue["id"]
            and tl.get("summary") == "Form validation and API integration testing"
        ):
            if tl.get("timeSpent") != 28800:
                errors.append(
                    f"Timelog timeSpent is {tl.get('timeSpent')}, expected 28800 (8 hours)."
                )
            found_timelog = True
            break
    if not found_timelog:
        errors.append(
            "No timelog with summary 'Form validation and API integration testing' found."
        )

    # Check health status
    if issue.get("healthStatus") != "at_risk":
        errors.append(
            f"Issue health is '{issue.get('healthStatus')}', expected 'at_risk'."
        )

    # Check weight
    if issue.get("weight") != 13:
        errors.append(f"Issue weight is {issue.get('weight')}, expected 13.")

    if errors:
        return False, " ".join(errors)

    return True, (
        "8-hour timelog added to user settings migration issue; "
        "health set to at_risk, weight set to 13."
    )
