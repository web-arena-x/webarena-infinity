import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find cadence "Hotfix Cadence" in iterationCadences
    hotfix_cadence = None
    for cadence in state.get("iterationCadences", []):
        if cadence.get("title") == "Hotfix Cadence":
            hotfix_cadence = cadence
            break
    if hotfix_cadence is None:
        return False, "Could not find iteration cadence 'Hotfix Cadence'."

    # Check durationWeeks == 1
    if hotfix_cadence.get("durationWeeks") != 1:
        return False, f"Cadence 'Hotfix Cadence' has durationWeeks={hotfix_cadence.get('durationWeeks')}, expected 1."

    # Check automatic == True
    if hotfix_cadence.get("automatic") is not True:
        return False, f"Cadence 'Hotfix Cadence' does not have automatic scheduling enabled."

    cadence_id = hotfix_cadence["id"]

    # Find iteration "Hotfix 1"
    hotfix_iteration = None
    for iteration in state.get("iterations", []):
        if iteration.get("title") == "Hotfix 1":
            hotfix_iteration = iteration
            break
    if hotfix_iteration is None:
        return False, "Could not find iteration 'Hotfix 1'."

    # Check cadenceId
    if hotfix_iteration.get("cadenceId") != cadence_id:
        return False, f"Iteration 'Hotfix 1' does not belong to cadence 'Hotfix Cadence'."

    # Check startDate
    if hotfix_iteration.get("startDate") != "2026-03-03":
        return False, f"Iteration 'Hotfix 1' has startDate='{hotfix_iteration.get('startDate')}', expected '2026-03-03'."

    # Check dueDate
    if hotfix_iteration.get("dueDate") != "2026-03-09":
        return False, f"Iteration 'Hotfix 1' has dueDate='{hotfix_iteration.get('dueDate')}', expected '2026-03-09'."

    return True, "Cadence 'Hotfix Cadence' created with 1-week automatic scheduling, and iteration 'Hotfix 1' created correctly."
