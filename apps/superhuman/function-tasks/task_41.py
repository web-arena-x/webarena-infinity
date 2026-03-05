import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})
    reminders = settings.get("reminders", {})
    default_time = reminders.get("defaultTime")

    if default_time == "14:00":
        return True, "Reminder default time successfully changed to '14:00'."

    return False, (
        f"reminders.defaultTime is '{default_time}', expected '14:00'."
    )
