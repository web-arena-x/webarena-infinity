import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    emails = state.get("emails", [])

    target_email = None
    for email in emails:
        subject = email.get("subject", "")
        if "Lose 30 pounds in 30 days" in subject:
            target_email = email
            break

    if not target_email:
        return False, "No email found with subject containing 'Lose 30 pounds in 30 days'."

    if target_email.get("isSpam") is not False:
        return False, f"Email isSpam is {target_email.get('isSpam')}, expected False."

    email_labels = target_email.get("labels", [])

    if "INBOX" not in email_labels:
        return False, f"Email does not have 'INBOX' in its labels: {email_labels}"

    if "label_7" not in email_labels:
        return False, f"Email does not have 'label_7' (Health) in its labels: {email_labels}"

    return True, "Task completed successfully."
