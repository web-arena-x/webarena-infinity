import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    reminders = state.get("reminders", [])

    if not reminders:
        return False, "No reminders found in state."

    count = len(reminders)
    unacknowledged = []
    for reminder in reminders:
        if reminder.get("acknowledged") is not True:
            unacknowledged.append(reminder.get("id", "unknown"))

    if unacknowledged:
        return False, (
            f"{len(unacknowledged)} of {count} reminders are still not acknowledged: "
            f"{', '.join(unacknowledged)}."
        )

    return True, f"All {count} reminders have been acknowledged."
