import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find Sprint 27
    sprint27 = None
    for it in state.get("iterations", []):
        if it.get("title") == "Sprint 27":
            sprint27 = it
            break
    if sprint27 is None:
        return False, "Could not find iteration 'Sprint 27'."

    sprint27_id = sprint27["id"]

    # Expected issues: Sprint 26 open issues with due date before 2026-03-02
    # issue_14 "Upgrade vulnerable deps" dueDate 2026-03-01
    # issue_17 "Login page blank screen" dueDate 2026-02-28
    # issue_27 "Optimize issue list query" dueDate 2026-03-01
    expected_titles = [
        "Upgrade vulnerable dependencies identified in audit",
        "Login page shows blank screen on Safari 17.2",
        "Optimize issue list query to use keyset pagination",
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
        if issue.get("healthStatus") != "at_risk":
            errors.append(f"Issue '{title}' health is '{issue.get('healthStatus')}', expected 'at_risk'.")
        if issue.get("iterationId") != sprint27_id:
            errors.append(f"Issue '{title}' not moved to Sprint 27.")

    if errors:
        return False, " ".join(errors)

    return True, f"All {len(expected_titles)} overdue Sprint 26 issues set to 'at risk' and moved to Sprint 27."
