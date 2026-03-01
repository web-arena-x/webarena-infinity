import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find the GraphQL gateway issue
    target_issue = None
    for issue in state.get("issues", []):
        if issue.get("title") == "Implement GraphQL gateway for v3 API":
            target_issue = issue
            break
    if target_issue is None:
        return False, "Could not find issue 'Implement GraphQL gateway for v3 API'."

    issue_id = target_issue["id"]

    # Check health status
    if target_issue.get("healthStatus") != "needs_attention":
        return False, f"Health status is '{target_issue.get('healthStatus')}', expected 'needs_attention'."

    # Check for a timelog with 3 hours (10800s) and matching summary
    timelogs = [t for t in state.get("timelogs", []) if t.get("issueId") == issue_id]
    matching = [t for t in timelogs if t.get("timeSpent") == 10800
                and "Schema validation review" in t.get("summary", "")]
    if not matching:
        return False, "No timelog found with 3 hours and summary containing 'Schema validation review'."

    return True, "GraphQL gateway issue has 3h timelog with correct summary and health status set to needs_attention."
