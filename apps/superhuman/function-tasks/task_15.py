import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    emails = state.get("emails", [])

    target_subject = "SolarPeak integration"
    email = next((e for e in emails if target_subject in e.get("subject", "")), None)

    if email is None:
        return False, f"Could not find email with subject containing '{target_subject}'."

    reminder = email.get("reminder")
    if reminder is None:
        return False, f"Email '{target_subject}' has no reminder set, expected a reminder for March 10."

    reminder_date = reminder.get("date", "")
    if "2026-03-10" not in reminder_date:
        return False, f"Email '{target_subject}' reminder date is '{reminder_date}', expected it to contain '2026-03-10'."

    return True, f"Email '{target_subject}' has a reminder set for March 10, 2026."
