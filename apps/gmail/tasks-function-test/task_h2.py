import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    emails = state.get("emails", [])
    if not emails:
        return False, "No emails found in state."

    target_email = None
    for email in emails:
        if email.get("isSent") is True and email.get("subject") == "Collaboration Meeting":
            target_email = email
            break

    if not target_email:
        return False, "No sent email found with subject 'Collaboration Meeting'."

    to_list = target_email.get("to", [])
    to_emails = [
        (r.get("email", "") if isinstance(r, dict) else r).lower()
        for r in to_list
    ]

    if "jennifer.wu@biomedresearch.com" not in to_emails:
        return False, f"Email 'to' field does not contain 'jennifer.wu@biomedresearch.com'. Found: {to_list}"

    cc_list = target_email.get("cc", [])
    cc_emails = [
        (r.get("email", "") if isinstance(r, dict) else r).lower()
        for r in cc_list
    ]

    if "kevin.zhao@quantumlab.tech" not in cc_emails:
        return False, f"Email 'cc' field does not contain 'kevin.zhao@quantumlab.tech'. Found: {cc_list}"

    body = (target_email.get("body") or "").lower()
    if "schedule a meeting" not in body:
        return False, "Email body does not contain 'schedule a meeting'."

    return True, "Task completed successfully."
