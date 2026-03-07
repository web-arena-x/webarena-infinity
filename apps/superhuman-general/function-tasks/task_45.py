import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})
    notifications = settings.get("notifications", {})
    alert_minutes = notifications.get("alertMinutes")

    if alert_minutes != 30:
        return False, f"Expected notifications.alertMinutes to be 30, got {alert_minutes}."

    return True, "Calendar alert timing changed to 30 minutes before."
