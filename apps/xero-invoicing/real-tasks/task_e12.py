import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    reminders = state.get("invoiceReminders", [])

    reminder = next((r for r in reminders if r.get("timing") == "before" and r.get("days") == 7), None)
    if reminder is None:
        return False, "7-day advance reminder (timing='before', days=7) not found."

    if reminder.get("enabled") is not False:
        return False, f"Expected 7-day advance reminder to be disabled (enabled=False), got enabled={reminder.get('enabled')}."

    return True, "7-day advance reminder has been disabled successfully."
