import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    emails = state.get("emails", [])

    target_subject = "Reminder: TechCorp domain"
    email = next((e for e in emails if target_subject in e.get("subject", "")), None)

    if email is None:
        return False, f"Could not find email with subject containing '{target_subject}'."

    if email.get("folder") != "spam":
        return False, f"Email '{target_subject}' folder is '{email.get('folder')}', expected 'spam'."

    return True, f"Email '{target_subject}' has been moved to spam."
