import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    emails = state.get("emails", [])

    target_subject = "Team Sync Follow-up"
    target_recipient = "jamie.chen@techcorp.io"

    # Find a sent email with the target subject
    sent_email = next(
        (e for e in emails
         if target_subject in e.get("subject", "")
         and e.get("folder") == "sent"),
        None
    )

    if sent_email is None:
        return False, f"Could not find a sent email with subject containing '{target_subject}'."

    # Check that the recipient is jamie.chen@techcorp.io
    to_list = sent_email.get("to", [])
    # to can be a list of objects {name, email} or a list of strings
    recipient_emails = []
    for recipient in to_list:
        if isinstance(recipient, dict):
            recipient_emails.append(recipient.get("email", ""))
        elif isinstance(recipient, str):
            recipient_emails.append(recipient)

    if target_recipient not in recipient_emails:
        return False, (
            f"Sent email '{target_subject}' recipients are {recipient_emails}, "
            f"expected '{target_recipient}' to be included."
        )

    return True, f"Email '{target_subject}' sent to '{target_recipient}' found in sent folder."
