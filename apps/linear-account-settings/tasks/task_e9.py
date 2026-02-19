import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify that the 'Notification badge' desktop setting is disabled."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    prefs = state.get("preferences", {})
    badge = prefs.get("notificationBadge")

    if badge is not False:
        return False, f"Expected notificationBadge=false, got {badge}."

    return True, "'Notification badge' successfully disabled."
