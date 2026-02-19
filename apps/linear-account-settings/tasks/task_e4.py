import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify that 'Display full names' is turned off."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    prefs = state.get("preferences", {})
    display_full = prefs.get("displayFullNames")

    if display_full is not False:
        return False, f"Expected displayFullNames=false, got {display_full}."

    return True, "'Display full names' successfully turned off."
