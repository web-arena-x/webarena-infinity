import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    emails = state.get("emails", [])

    violating = []
    for email in emails:
        category = (email.get("category") or "").lower()
        is_read = email.get("isRead", False)
        labels = email.get("labels", [])
        if category == "social" and is_read is False and "INBOX" in labels:
            violating.append(email.get("subject", "(no subject)"))

    if violating:
        return False, f"Found {len(violating)} unread Social email(s) still in inbox: {violating}"

    return True, "Task completed successfully."
