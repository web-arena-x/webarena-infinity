import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    emails = state.get("emails", [])
    blocked_senders = state.get("blockedSenders", [])

    # Check that hello@englw.com is in blocked senders
    target_sender = "hello@englw.com"
    blocked_emails = [b.get("email", "") for b in blocked_senders]
    if target_sender not in blocked_emails:
        return False, f"Sender '{target_sender}' is not in blockedSenders list: {blocked_emails}."

    # Check that the email has been moved out of inbox (to done)
    target_subject = "Engineering Manager spotlight"
    email = next((e for e in emails if target_subject in e.get("subject", "")), None)

    if email is None:
        return False, f"Could not find email with subject containing '{target_subject}'."

    if email.get("folder") != "done":
        return False, f"Email '{target_subject}' folder is '{email.get('folder')}', expected 'done' after unsubscribe."

    return True, f"Sender '{target_sender}' is blocked and email '{target_subject}' moved to done."
