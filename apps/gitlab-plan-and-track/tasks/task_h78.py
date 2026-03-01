import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find 'Tech Debt Sprint' milestone
    td_ms = None
    for m in state.get("milestones", []):
        if m.get("title") == "Tech Debt Sprint":
            td_ms = m
            break
    if td_ms is None:
        return False, "Could not find milestone 'Tech Debt Sprint'."

    errors = []

    if td_ms.get("startDate") != "2026-03-17":
        errors.append(
            f"Milestone start date is '{td_ms.get('startDate')}', expected '2026-03-17'."
        )
    if td_ms.get("dueDate") != "2026-03-28":
        errors.append(
            f"Milestone due date is '{td_ms.get('dueDate')}', expected '2026-03-28'."
        )

    # Find technical-debt label
    td_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "technical-debt":
            td_label = lbl
            break
    if td_label is None:
        return False, "Could not find label 'technical-debt'."

    # Open issues with technical-debt should be in Tech Debt Sprint with needs_attention
    expected_titles = [
        "Refactor notification service to use event-driven architecture",
        "Replace deprecated analytics library",
    ]

    for title in expected_titles:
        issue = None
        for i in state.get("issues", []):
            if i.get("title") == title:
                issue = i
                break
        if issue is None:
            errors.append(f"Could not find issue '{title}'.")
            continue
        if issue.get("milestoneId") != td_ms["id"]:
            errors.append(f"Issue '{title}' not in 'Tech Debt Sprint' milestone.")
        if issue.get("healthStatus") != "needs_attention":
            errors.append(
                f"Issue '{title}' health is '{issue.get('healthStatus')}', "
                f"expected 'needs_attention'."
            )

    if errors:
        return False, " ".join(errors)

    return True, (
        f"Tech Debt Sprint milestone created; "
        f"{len(expected_titles)} issues moved in with needs_attention health."
    )
