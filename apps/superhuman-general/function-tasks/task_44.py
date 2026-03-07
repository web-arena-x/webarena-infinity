import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})
    notifications = settings.get("notifications", {})
    calendar_alerts = notifications.get("calendarAlerts")

    if calendar_alerts is not False:
        return False, f"Expected notifications.calendarAlerts to be False, got {calendar_alerts}."

    return True, "Calendar alerts are disabled."
