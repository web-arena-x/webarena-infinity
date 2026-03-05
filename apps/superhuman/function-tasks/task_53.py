import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that event notifications have been changed to '30-minutes'."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()

    try:
        notifications = state["settings"]["calendar"]["eventNotifications"]
    except (KeyError, TypeError) as e:
        return False, f"Could not find settings.calendar.eventNotifications: {e}"

    if notifications == "30-minutes":
        return True, "Event notifications are set to '30-minutes'."
    return False, f"Expected settings.calendar.eventNotifications to be '30-minutes', got {notifications!r}."
