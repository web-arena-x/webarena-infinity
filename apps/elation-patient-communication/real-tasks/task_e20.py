import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    reminders = state.get("reminders", [])
    for reminder in reminders:
        if reminder.get("id") == "rem_5":
            if reminder.get("acknowledged") is True:
                return True, "Martha Reeves-Whitfield's appointment reminder has been acknowledged."
            else:
                return False, f"Reminder rem_5 found but acknowledged is {reminder.get('acknowledged')}, expected True."

    return False, "Reminder with id 'rem_5' not found in reminders."
