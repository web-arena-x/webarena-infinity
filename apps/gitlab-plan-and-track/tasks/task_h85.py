import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # Q1 2026 Planning milestone should be closed
    q1_ms = None
    for m in state.get("milestones", []):
        if m.get("title") == "Q1 2026 Planning":
            q1_ms = m
            break
    if q1_ms is None:
        return False, "Could not find milestone 'Q1 2026 Planning'."

    if q1_ms.get("status") != "closed":
        errors.append(
            f"Q1 2026 Planning status is '{q1_ms.get('status')}', expected 'closed'."
        )

    # Find v4.1 - Performance milestone
    perf_ms = None
    for m in state.get("milestones", []):
        if m.get("title") == "v4.1 - Performance":
            perf_ms = m
            break
    if perf_ms is None:
        return False, "Could not find milestone 'v4.1 - Performance'."

    # Both documentation issues should be in v4.1 - Performance
    expected_titles = [
        "Write getting started guide for new developers",
        "Create API reference documentation with examples",
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
        if issue.get("milestoneId") != perf_ms["id"]:
            errors.append(
                f"Issue '{title}' milestoneId is '{issue.get('milestoneId')}', "
                f"expected '{perf_ms['id']}'."
            )

    if errors:
        return False, " ".join(errors)

    return True, (
        "Q1 2026 Planning milestone closed; "
        "its issues moved to v4.1 - Performance."
    )
