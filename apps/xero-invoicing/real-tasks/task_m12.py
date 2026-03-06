import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    reminders = state.get("invoiceReminders", [])
    for r in reminders:
        if r.get("timing") == "after" and r.get("days") == 14:
            return False, "14-day overdue reminder still exists."

    return True, "14-day overdue reminder has been deleted."
