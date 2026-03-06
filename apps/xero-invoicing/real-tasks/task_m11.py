import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    reminders = state.get("invoiceReminders", [])
    found = False
    for r in reminders:
        if r.get("timing") == "after" and r.get("days") == 21:
            found = True
            break

    if not found:
        return False, f"No reminder found with timing='after' and days=21. Current reminders: {reminders}"

    return True, "Reminder for 21 days after due date has been created."
