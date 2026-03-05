"""Task H4: Empty the spam folder and unblock spam@fakecorp.com."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    # Check no emails remain in spam folder
    spam_emails = [e for e in state.get("emails", []) if e.get("folder") == "spam"]
    if spam_emails:
        spam_ids = [e["id"] for e in spam_emails]
        return False, f"Spam folder still has {len(spam_emails)} email(s): {spam_ids}"

    # Check spam@fakecorp.com is not in blocked senders
    blocked_senders = state.get("blockedSenders", [])
    for sender in blocked_senders:
        sender_email = sender.get("email", "") if isinstance(sender, dict) else sender
        if sender_email == "spam@fakecorp.com":
            return False, "spam@fakecorp.com is still in blockedSenders."

    return True, "Spam folder emptied and spam@fakecorp.com unblocked."
