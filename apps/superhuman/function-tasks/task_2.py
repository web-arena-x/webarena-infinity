import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    emails = state.get("emails", [])

    target_subject = "Q1 OKR mid-quarter check-in"
    email = next((e for e in emails if target_subject in e.get("subject", "")), None)

    if email is None:
        return False, f"Could not find email with subject containing '{target_subject}'."

    if email.get("isRead") is not False:
        return False, f"Email '{target_subject}' isRead is {email.get('isRead')}, expected False."

    return True, f"Email '{target_subject}' is marked as unread."
