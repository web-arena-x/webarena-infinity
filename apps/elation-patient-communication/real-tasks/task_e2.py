import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that the appointment reminder for James Rodriguez is acknowledged."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    reminders = state.get("reminders", [])
    reminder = None
    for rem in reminders:
        if rem.get("id") == "rem_10":
            reminder = rem
            break

    if reminder is None:
        return False, "Reminder rem_10 (appointment reminder for James Rodriguez) not found"

    if not reminder.get("acknowledged"):
        return False, f"Reminder rem_10 acknowledged is {reminder.get('acknowledged')}, expected True"

    return True, "Appointment reminder for James Rodriguez (rem_10) is acknowledged"
