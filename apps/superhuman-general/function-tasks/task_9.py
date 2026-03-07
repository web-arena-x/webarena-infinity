import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    emails = state.get("emails", [])

    email = next(
        (e for e in emails if e["subject"] == "Patent Filing Deadline - April 15"
         and e["from"]["name"] == "James O'Brien"),
        None,
    )
    if email is None:
        return False, "Could not find email 'Patent Filing Deadline - April 15' from James O'Brien."

    remind_at = email.get("remindAt")
    if remind_at is not None:
        return False, f"Reminder on 'Patent Filing Deadline - April 15' was not cleared. remindAt={remind_at}"

    return True, "Reminder cleared from email 'Patent Filing Deadline - April 15' from James O'Brien."
