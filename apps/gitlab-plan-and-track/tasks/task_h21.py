import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find Sprint 27
    sprint27 = None
    for iteration in state.get("iterations", []):
        if iteration.get("title") == "Sprint 27":
            sprint27 = iteration
            break
    if sprint27 is None:
        return False, "Could not find iteration 'Sprint 27'."
    sprint27_id = sprint27["id"]

    # Find all open issues in Sprint 27
    sprint27_issues = []
    for issue in state.get("issues", []):
        if issue.get("iterationId") == sprint27_id and issue.get("status") == "open":
            sprint27_issues.append(issue)

    if len(sprint27_issues) < 3:
        return False, f"Expected at least 3 open issues in Sprint 27, found {len(sprint27_issues)}."

    # Check each has health status 'on_track'
    errors = []
    for issue in sprint27_issues:
        if issue.get("healthStatus") != "on_track":
            errors.append(f"{issue.get('title')} (healthStatus={issue.get('healthStatus')})")

    if errors:
        return False, f"These Sprint 27 issues don't have healthStatus 'on_track': {errors}"

    return True, f"All {len(sprint27_issues)} open issues in Sprint 27 have health status 'on track'."
