import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})
    reminders = settings.get("reminders", {})
    auto_reminders = reminders.get("autoReminders")

    if auto_reminders == "external-only":
        return True, "Auto-reminders successfully changed to 'external-only'."

    return False, (
        f"reminders.autoReminders is '{auto_reminders}', expected 'external-only'."
    )
