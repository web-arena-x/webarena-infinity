import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that the unread alert reminder about Maria Gonzalez's lab results is acknowledged."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    reminders = state.get("reminders", [])
    reminder = None
    for rem in reminders:
        if rem.get("id") == "rem_1":
            reminder = rem
            break

    if reminder is None:
        return False, "Reminder rem_1 (unread alert for Maria Gonzalez's lab results) not found"

    if not reminder.get("acknowledged"):
        return False, f"Reminder rem_1 acknowledged is {reminder.get('acknowledged')}, expected True"

    return True, "Unread alert reminder about Maria Gonzalez's lab results (rem_1) is acknowledged"
