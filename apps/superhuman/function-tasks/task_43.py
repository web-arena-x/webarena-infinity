import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})
    reminders = settings.get("reminders", {})
    auto_reminder_delay = reminders.get("autoReminderDelay")

    if auto_reminder_delay == 5:
        return True, "Auto-reminder delay successfully changed to 5 days."

    return False, (
        f"reminders.autoReminderDelay is {auto_reminder_delay}, expected 5."
    )
