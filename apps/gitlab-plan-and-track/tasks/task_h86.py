import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # Find Release Cycle cadence
    rc_cadence = None
    for c in state.get("iterationCadences", []):
        if c.get("title") == "Release Cycle":
            rc_cadence = c
            break
    if rc_cadence is None:
        return False, "Could not find cadence 'Release Cycle'."

    # Find 'Release 4.0 GA' iteration
    ga_iter = None
    for it in state.get("iterations", []):
        if it.get("title") == "Release 4.0 GA":
            ga_iter = it
            break
    if ga_iter is None:
        return False, "Could not find iteration 'Release 4.0 GA'."

    if ga_iter.get("cadenceId") != rc_cadence["id"]:
        errors.append(
            f"Iteration cadenceId is '{ga_iter.get('cadenceId')}', "
            f"expected '{rc_cadence['id']}'."
        )
    if ga_iter.get("startDate") != "2026-03-01":
        errors.append(
            f"Iteration start date is '{ga_iter.get('startDate')}', expected '2026-03-01'."
        )
    if ga_iter.get("dueDate") != "2026-03-15":
        errors.append(
            f"Iteration due date is '{ga_iter.get('dueDate')}', expected '2026-03-15'."
        )

    # CSP headers and vulnerable deps should be assigned to this iteration
    expected_titles = [
        "Implement Content Security Policy headers",
        "Upgrade vulnerable dependencies identified in audit",
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
        if issue.get("iterationId") != ga_iter["id"]:
            errors.append(
                f"Issue '{title}' iterationId is '{issue.get('iterationId')}', "
                f"expected '{ga_iter['id']}'."
            )

    if errors:
        return False, " ".join(errors)

    return True, (
        "Iteration 'Release 4.0 GA' created in Release Cycle cadence; "
        "CSP headers and vulnerable deps issues assigned to it."
    )
