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
    errors = []

    # Check for a timelog with 2 hours (7200s) and matching summary
    timelogs = [t for t in state.get("timelogs", []) if t.get("issueId") == issue_id]
    matching = [t for t in timelogs if t.get("timeSpent") == 7200
                and "Security review" in t.get("summary", "")]
    if not matching:
        errors.append("No timelog found with 2 hours and summary containing 'Security review'.")

    # Find Sprint 28
    sprint28 = None
    for iteration in state.get("iterations", []):
        if iteration.get("title") == "Sprint 28":
            sprint28 = iteration
            break
    if sprint28 is None:
        return False, "Could not find iteration 'Sprint 28'."

    # Check iteration
    if target_issue.get("iterationId") != sprint28["id"]:
        errors.append(f"Issue iteration is '{target_issue.get('iterationId')}', expected Sprint 28 ('{sprint28['id']}').")

    if errors:
        return False, " ".join(errors)

    return True, "CSP headers issue has 2h timelog with 'Security review' summary and moved to Sprint 28."
