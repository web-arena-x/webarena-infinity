import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find the Release Cycle cadence
    release_cadence = None
    for cad in state.get("iterationCadences", []):
        if cad.get("title") == "Release Cycle":
            release_cadence = cad
            break
    if release_cadence is None:
        return False, "Could not find cadence 'Release Cycle'."

    # Find the Release 4.0 GA iteration
    target_iter = None
    for iteration in state.get("iterations", []):
        if iteration.get("title") == "Release 4.0 GA":
            target_iter = iteration
            break
    if target_iter is None:
        return False, "Could not find iteration 'Release 4.0 GA'."

    if target_iter.get("cadenceId") != release_cadence["id"]:
        return False, f"Iteration cadenceId is '{target_iter.get('cadenceId')}', expected '{release_cadence['id']}'."

    if target_iter.get("startDate") != "2026-03-01":
        return False, f"Iteration startDate is '{target_iter.get('startDate')}', expected '2026-03-01'."

    if target_iter.get("dueDate") != "2026-03-15":
        return False, f"Iteration dueDate is '{target_iter.get('dueDate')}', expected '2026-03-15'."

    return True, "Iteration 'Release 4.0 GA' created in Release Cycle cadence with correct dates."
