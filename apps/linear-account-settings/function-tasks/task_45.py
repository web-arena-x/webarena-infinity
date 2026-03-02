import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify communicationPreferences.communityUpdates is True."""
    try:
        resp = requests.get(f"{server_url}/api/state", timeout=5)
        resp.raise_for_status()
        state = resp.json()
    except Exception as e:
        return False, f"Failed to fetch state: {e}"

    prefs = state.get("communicationPreferences")
    if not prefs:
        return False, "communicationPreferences not found in state."

    value = prefs.get("communityUpdates")
    if value is not True:
        return False, f"communityUpdates is {value}, expected True."

    return True, "communicationPreferences.communityUpdates is True."
