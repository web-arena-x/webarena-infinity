import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find David Kim
    david = None
    for user in state.get("users", []):
        if user.get("name") == "David Kim":
            david = user
            break
    if david is None:
        return False, "Could not find user 'David Kim'."
    david_id = david["id"]

    # Find the 'blocked' label
    blocked_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "blocked":
            blocked_label = lbl
            break
    if blocked_label is None:
        return False, "Could not find label 'blocked'."
    blocked_id = blocked_label["id"]

    # Find all open issues assigned to David Kim
    david_issues = []
    for issue in state.get("issues", []):
        if issue.get("status") == "open" and david_id in issue.get("assignees", []):
            david_issues.append(issue)

    if len(david_issues) < 3:
        return False, f"Expected at least 3 open issues assigned to David Kim, found {len(david_issues)}."

    # Check each has health status 'needs_attention' and 'blocked' label
    errors = []
    for issue in david_issues:
        problems = []
        if issue.get("healthStatus") != "needs_attention":
            problems.append(f"healthStatus={issue.get('healthStatus')}")
        if blocked_id not in issue.get("labels", []):
            problems.append("missing 'blocked' label")
        if problems:
            errors.append(f"{issue.get('title')}: {', '.join(problems)}")

    if errors:
        return False, f"Issues with incorrect state: {errors}"

    return True, f"All {len(david_issues)} open issues assigned to David Kim have 'needs attention' health status and 'blocked' label."
