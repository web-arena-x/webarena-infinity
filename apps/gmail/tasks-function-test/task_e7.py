import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    emails = state.get("emails", [])
    target_substring = "Meeting notes: Sprint planning"

    for email in emails:
        subject = email.get("subject", "")
        if target_substring in subject:
            labels = email.get("labels", [])
            is_archived = email.get("isArchived", False)

            if "INBOX" not in labels:
                return False, f"Email '{subject}' does not have 'INBOX' label. Current labels: {labels}."
            if is_archived:
                return False, f"Email '{subject}' is still archived (isArchived=True)."
            return True, "Task completed successfully."

    return False, f"Email with subject containing '{target_substring}' not found."
