import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    iterations = state.get("iterations", [])
    cadences = state.get("iterationCadences", [])

    release_cadence = next((c for c in cadences if c["title"] == "Release Cycle"), None)
    if not release_cadence:
        return False, "Iteration cadence with title 'Release Cycle' not found."

    target = next((it for it in iterations if it["title"] == "Release 4.0 GA"), None)
    if not target:
        return False, "Iteration with title 'Release 4.0 GA' not found."

    if target.get("cadenceId") != release_cadence["id"]:
        return False, f"Iteration cadenceId is '{target.get('cadenceId')}', expected '{release_cadence['id']}'."

    if target.get("startDate") != "2026-03-01":
        return False, f"Iteration startDate is '{target.get('startDate')}', expected '2026-03-01'."

    if target.get("dueDate") != "2026-03-15":
        return False, f"Iteration dueDate is '{target.get('dueDate')}', expected '2026-03-15'."

    return True, "Iteration 'Release 4.0 GA' exists under 'Release Cycle' cadence with correct dates."
