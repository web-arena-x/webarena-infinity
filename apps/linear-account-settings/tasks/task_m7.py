import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify that both auto-assign settings are enabled."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    prefs = state.get("preferences", {})

    auto_create = prefs.get("autoAssignOnCreate")
    auto_started = prefs.get("autoAssignOnStarted")

    if auto_create is not True:
        return False, f"Expected autoAssignOnCreate=true, got {auto_create}."
    if auto_started is not True:
        return False, f"Expected autoAssignOnStarted=true, got {auto_started}."

    return True, "Both auto-assign settings successfully enabled."
