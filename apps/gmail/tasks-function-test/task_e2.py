import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    emails = state.get("emails", [])
    target_subject = "You have inherited $5,000,000"

    for email in emails:
        if email.get("subject") == target_subject:
            is_trashed = email.get("isTrashed", False)
            labels = email.get("labels", [])

            if is_trashed:
                return False, f"Email '{target_subject}' is still in Trash (isTrashed=True)."
            if "INBOX" not in labels:
                return False, f"Email '{target_subject}' does not have 'INBOX' label. Current labels: {labels}."
            return True, "Task completed successfully."

    return False, f"Email with subject '{target_subject}' not found."
