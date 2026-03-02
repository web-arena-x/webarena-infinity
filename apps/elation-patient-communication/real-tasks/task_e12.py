import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    reminders = state.get("reminders", [])
    for reminder in reminders:
        if reminder.get("id") == "rem_7":
            if reminder.get("acknowledged") is True:
                return True, "Marcus Johnson's Passport reminder has been acknowledged."
            else:
                return False, f"Reminder rem_7 found but acknowledged is {reminder.get('acknowledged')}, expected True."

    return False, "Reminder with id 'rem_7' not found in reminders."
