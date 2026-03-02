import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    val = state["preferences"]["automationsAndWorkflows"]["autoAssignOnStarted"]
    if val is not True:
        return False, f"Expected autoAssignOnStarted to be True, got '{val}'."

    return True, "Auto-assign on started enabled."
