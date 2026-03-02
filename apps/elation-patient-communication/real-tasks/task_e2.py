import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    reminders = state.get("reminders", [])
    for reminder in reminders:
        if reminder.get("id") == "rem_4":
            if reminder.get("acknowledged") is True:
                return True, "Aisha Patel's appointment reminder has been acknowledged."
            else:
                return False, f"Reminder rem_4 found but acknowledged is {reminder.get('acknowledged')}, expected True."

    return False, "Reminder with id 'rem_4' not found in reminders."
