import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    violating_emails = []
    for email in state.get("emails", []):
        category = email.get("category", "")
        is_read = email.get("isRead", True)
        labels = email.get("labels", [])

        if category == "promotions" and not is_read and "INBOX" in labels:
            violating_emails.append(email.get("subject", "(no subject)"))

    if not violating_emails:
        return True, "Task completed successfully."
    else:
        return False, f"Found {len(violating_emails)} unread promotion email(s) still in INBOX: {violating_emails}."
