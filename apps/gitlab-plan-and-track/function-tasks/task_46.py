import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    cadences = state.get("iterationCadences", [])

    target = next((c for c in cadences if c["title"] == "Bug Fix Cadence"), None)
    if not target:
        return False, "Iteration cadence with title 'Bug Fix Cadence' not found."

    if target.get("automatic") is not True:
        return False, f"Cadence 'automatic' is {target.get('automatic')}, expected True."

    if target.get("durationWeeks") != 1:
        return False, f"Cadence 'durationWeeks' is {target.get('durationWeeks')}, expected 1."

    if target.get("upcomingIterations") != 4:
        return False, f"Cadence 'upcomingIterations' is {target.get('upcomingIterations')}, expected 4."

    return True, "Iteration cadence 'Bug Fix Cadence' exists with automatic=True, durationWeeks=1, upcomingIterations=4."
