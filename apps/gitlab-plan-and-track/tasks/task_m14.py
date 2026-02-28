import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    iterations = state.get("iterations", [])
    iteration = next((it for it in iterations if it.get("title") == "Sprint 29"), None)
    if iteration is None:
        return False, "Could not find iteration titled 'Sprint 29'."

    cadences = state.get("iterationCadences", [])
    cadence = next((c for c in cadences if c.get("title") == "Sprint Cadence"), None)
    if cadence is None:
        return False, "Could not find iteration cadence titled 'Sprint Cadence'."

    if iteration.get("cadenceId") != cadence.get("id"):
        return False, f"Iteration's cadenceId '{iteration.get('cadenceId')}' does not match 'Sprint Cadence' id '{cadence.get('id')}'."

    if iteration.get("startDate") != "2026-03-31":
        return False, f"Expected startDate '2026-03-31' but got '{iteration.get('startDate')}'."

    if iteration.get("dueDate") != "2026-04-13":
        return False, f"Expected dueDate '2026-04-13' but got '{iteration.get('dueDate')}'."

    return True, "Iteration 'Sprint 29' created in Sprint Cadence with correct start date (2026-03-31) and due date (2026-04-13)."
