import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify communicationPreferences.productAnnouncements is False."""
    try:
        resp = requests.get(f"{server_url}/api/state", timeout=5)
        resp.raise_for_status()
        state = resp.json()
    except Exception as e:
        return False, f"Failed to fetch state: {e}"

    prefs = state.get("communicationPreferences")
    if not prefs:
        return False, "communicationPreferences not found in state."

    value = prefs.get("productAnnouncements")
    if value is not False:
        return False, f"productAnnouncements is {value}, expected False."

    return True, "communicationPreferences.productAnnouncements is False."
