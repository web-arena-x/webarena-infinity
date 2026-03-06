import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    reminders = state.get("invoiceReminders", [])

    reminder = next((r for r in reminders if r.get("timing") == "after" and r.get("days") == 30), None)
    if reminder is None:
        return False, "30-day overdue reminder (timing='after', days=30) not found."

    if reminder.get("enabled") is not True:
        return False, f"Expected 30-day overdue reminder to be enabled (enabled=True), got enabled={reminder.get('enabled')}."

    return True, "30-day overdue reminder has been enabled successfully."
