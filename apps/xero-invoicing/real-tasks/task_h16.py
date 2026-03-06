import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    reminders = state.get("invoiceReminders", [])

    # Check exactly 1 reminder exists with timing='before'
    before_reminders = [r for r in reminders if r.get("timing") == "before"]
    if len(before_reminders) != 1:
        return False, f"Expected exactly 1 reminder with timing='before', found {len(before_reminders)}."

    # Check no reminders with timing='after' exist
    after_reminders = [r for r in reminders if r.get("timing") == "after"]
    if len(after_reminders) > 0:
        return False, f"Expected 0 reminders with timing='after', found {len(after_reminders)}."

    # Check total is exactly 1
    if len(reminders) != 1:
        return False, f"Expected exactly 1 total reminder, found {len(reminders)}."

    return True, "All overdue reminders deleted. Only the before-due-date reminder remains."
