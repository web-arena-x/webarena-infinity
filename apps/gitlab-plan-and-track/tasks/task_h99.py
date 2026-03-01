import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # Find Release Cycle cadence
    rc_cad = None
    for c in state.get("iterationCadences", []):
        if c.get("title") == "Release Cycle":
            rc_cad = c
            break
    if rc_cad is None:
        return False, "Could not find cadence 'Release Cycle'."

    # Verify cadence settings
    if not rc_cad.get("automatic"):
        errors.append("Release Cycle automatic should be true.")
    if rc_cad.get("durationWeeks") != 4:
        errors.append(
            f"Release Cycle durationWeeks is {rc_cad.get('durationWeeks')}, expected 4."
        )
    if rc_cad.get("upcomingIterations") != 2:
        errors.append(
            f"Release Cycle upcomingIterations is {rc_cad.get('upcomingIterations')}, "
            f"expected 2."
        )

    # Find 'Release 4.1 Alpha' iteration
    alpha_iter = None
    for it in state.get("iterations", []):
        if it.get("title") == "Release 4.1 Alpha":
            alpha_iter = it
            break
    if alpha_iter is None:
        return False, "Could not find iteration 'Release 4.1 Alpha'. " + " ".join(errors)

    if alpha_iter.get("cadenceId") != rc_cad["id"]:
        errors.append(
            f"Iteration cadenceId is '{alpha_iter.get('cadenceId')}', "
            f"expected '{rc_cad['id']}'."
        )
    if alpha_iter.get("startDate") != "2026-03-15":
        errors.append(
            f"Iteration start date is '{alpha_iter.get('startDate')}', expected '2026-03-15'."
        )
    if alpha_iter.get("dueDate") != "2026-04-11":
        errors.append(
            f"Iteration due date is '{alpha_iter.get('dueDate')}', expected '2026-04-11'."
        )

    if errors:
        return False, " ".join(errors)

    return True, (
        "Release Cycle cadence updated to automatic with 4-week duration; "
        "Release 4.1 Alpha iteration created."
    )
