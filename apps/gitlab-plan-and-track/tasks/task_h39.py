import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find the Release Cycle cadence
    cadence = None
    for c in state.get("iterationCadences", []):
        if c.get("title") == "Release Cycle":
            cadence = c
            break
    if cadence is None:
        return False, "Could not find cadence 'Release Cycle'."

    errors = []

    if cadence.get("automatic") is not True:
        errors.append(f"Automatic is {cadence.get('automatic')}, expected True.")

    if cadence.get("startDate") != "2026-03-01":
        errors.append(f"Start date is '{cadence.get('startDate')}', expected '2026-03-01'.")

    if cadence.get("durationWeeks") != 4:
        errors.append(f"Duration is {cadence.get('durationWeeks')} weeks, expected 4.")

    if cadence.get("upcomingIterations") != 2:
        errors.append(f"Upcoming iterations is {cadence.get('upcomingIterations')}, expected 2.")

    if errors:
        return False, " ".join(errors)

    return True, "Release Cycle cadence updated: automatic scheduling, March 1 start, 4-week duration, 2 upcoming."
