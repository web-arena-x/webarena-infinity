import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    cadences = state.get("iterationCadences", [])
    cadence = next((c for c in cadences if c.get("title") == "Sprint Cadence"), None)
    if cadence is None:
        return False, "Could not find iteration cadence titled 'Sprint Cadence'."

    if cadence.get("automatic") != False:
        return False, f"Expected 'automatic' to be False but got '{cadence.get('automatic')}'."

    if cadence.get("rollOver") != False:
        return False, f"Expected 'rollOver' to be False but got '{cadence.get('rollOver')}'."

    return True, "Sprint Cadence has automatic scheduling and roll-over both disabled."
