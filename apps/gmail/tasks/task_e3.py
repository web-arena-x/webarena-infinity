import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    for email in state.get("emails", []):
        if email.get("subject") == "Shipping Update: Order #LP-2026-8834":
            labels = email.get("labels", [])
            is_archived = email.get("isArchived", False)
            inbox_removed = "INBOX" not in labels

            if inbox_removed or is_archived:
                return True, "Task completed successfully."
            else:
                return False, f"Email found but still in INBOX (labels={labels}, isArchived={is_archived})."

    return False, "Email with subject 'Shipping Update: Order #LP-2026-8834' not found."
