import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify emailDigestPreferences.sendImmediatelyOnUrgent is False."""
    try:
        resp = requests.get(f"{server_url}/api/state", timeout=5)
        resp.raise_for_status()
        state = resp.json()
    except Exception as e:
        return False, f"Failed to fetch state: {e}"

    prefs = state.get("emailDigestPreferences")
    if not prefs:
        return False, "emailDigestPreferences not found in state."

    value = prefs.get("sendImmediatelyOnUrgent")
    if value is not False:
        return False, f"sendImmediatelyOnUrgent is {value}, expected False."

    return True, "sendImmediatelyOnUrgent is False."
