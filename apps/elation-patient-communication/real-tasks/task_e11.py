import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that the passport invitation reminder for Marcus Johnson is acknowledged."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    reminders = state.get("reminders", [])
    reminder = None
    for rem in reminders:
        if rem.get("id") == "rem_7":
            reminder = rem
            break

    if reminder is None:
        return False, "Reminder rem_7 (passport invitation for Marcus Johnson) not found"

    if not reminder.get("acknowledged"):
        return False, f"Reminder rem_7 acknowledged is {reminder.get('acknowledged')}, expected True"

    return True, "Passport invitation reminder for Marcus Johnson (rem_7) is acknowledged"
