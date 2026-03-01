import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # Find Database Optimization epic
    db_epic = None
    for e in state.get("epics", []):
        if e.get("title") == "Database Optimization":
            db_epic = e
            break
    if db_epic is None:
        return False, "Could not find epic 'Database Optimization'."

    # Find Sprint 27
    sprint27 = None
    for it in state.get("iterations", []):
        if it.get("title") == "Sprint 27":
            sprint27 = it
            break
    if sprint27 is None:
        return False, "Could not find iteration 'Sprint 27'."

    # The two issues that were in Sprint 26 and Database Optimization epic
    expected_titles = [
        "Analyze and optimize slow queries from APM logs",
        "Optimize issue list query to use keyset pagination",
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
        if issue.get("iterationId") != sprint27["id"]:
            errors.append(
                f"Issue '{title}' iterationId is '{issue.get('iterationId')}', "
                f"expected '{sprint27['id']}'."
            )

    if errors:
        return False, " ".join(errors)

    return True, (
        "Both Database Optimization issues moved from Sprint 26 to Sprint 27."
    )
