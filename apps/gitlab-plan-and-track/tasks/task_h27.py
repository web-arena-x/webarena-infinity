import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Check no cadence named "Monthly Planning" exists
    for c in state.get("iterationCadences", []):
        if c.get("title") == "Monthly Planning":
            return False, "Cadence 'Monthly Planning' still exists (should be renamed)."

    # Find the renamed cadence
    cadence = None
    for c in state.get("iterationCadences", []):
        if c.get("title") == "Bi-Weekly Planning":
            cadence = c
            break
    if cadence is None:
        return False, "Could not find cadence 'Bi-Weekly Planning'."

    # Check duration
    if cadence.get("durationWeeks") != 2:
        return False, f"Cadence duration is {cadence.get('durationWeeks')} weeks, expected 2."

    return True, "Monthly Planning cadence renamed to 'Bi-Weekly Planning' with 2-week duration."
