import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    emails = state.get("emails", [])
    target_email = None
    for email in emails:
        if email.get("isSent") is True and email.get("subject") == "Guest Lecture Confirmation":
            target_email = email
            break

    if not target_email:
        return False, (
            "Could not find a sent email with subject 'Guest Lecture Confirmation'. "
            "Expected isSent=True and subject='Guest Lecture Confirmation'."
        )

    # Check recipient
    to_list = target_email.get("to", [])
    found_recipient = False
    for recipient in to_list:
        if isinstance(recipient, dict):
            addr = recipient.get("email", "").lower()
        elif isinstance(recipient, str):
            addr = recipient.lower()
        else:
            continue
        if addr == "robert.singh@university.edu":
            found_recipient = True
            break

    if not found_recipient:
        return False, (
            f"Sent email 'Guest Lecture Confirmation' does not have "
            f"'robert.singh@university.edu' in the 'to' list. Current to: {to_list}"
        )

    # Check body
    body = target_email.get("body", "")
    if "happy to give the guest lecture" not in body.lower():
        return False, (
            f"Sent email 'Guest Lecture Confirmation' body does not contain "
            f"'happy to give the guest lecture'. Body preview: {body[:200]}"
        )

    return True, "Task completed successfully."
