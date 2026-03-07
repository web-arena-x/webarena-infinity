import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    emails = state.get("emails", [])

    email = next(
        (e for e in emails if e["subject"] == "Quantum Computing Integration Prototype"
         and e["from"]["name"] == "Kevin Zhao"),
        None,
    )
    if email is None:
        return False, "Could not find email 'Quantum Computing Integration Prototype' from Kevin Zhao."

    remind_at = email.get("remindAt")
    if remind_at is None:
        return False, "Email 'Quantum Computing Integration Prototype' has no reminder set. remindAt is None."

    if "2026-03-08" not in str(remind_at):
        return False, f"Reminder is not set for tomorrow (2026-03-08). remindAt={remind_at}"

    return True, "Reminder set on 'Quantum Computing Integration Prototype' for 2026-03-08."
