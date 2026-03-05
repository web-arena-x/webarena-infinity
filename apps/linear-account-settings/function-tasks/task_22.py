import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    val = state["preferences"]["desktopApp"]["showNotificationBadge"]
    if val is not False:
        return False, f"Expected showNotificationBadge to be False, got '{val}'."

    return True, "Show notification badge disabled."
