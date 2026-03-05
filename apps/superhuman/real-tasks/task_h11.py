"""Task H11: Block the sender of every spam email and mark them all as read."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    # Spam email senders
    spam_senders = {
        "email_109": "info@wfh-earningsguide.com",
        "email_110": "noreply@fedex-delivery-update.net",
        "email_111": "alerts@domainrenewal-notice.info",
        "email_112": "deals@promos@cheapdeals.biz",
        "email_113": "rewards@apple-promo-center.net",
    }

    # Get blocked sender emails
    blocked_senders = state.get("blockedSenders", [])
    blocked_emails = set()
    for sender in blocked_senders:
        if isinstance(sender, dict):
            blocked_emails.add(sender.get("email", ""))
        else:
            blocked_emails.add(sender)

    emails_by_id = {e["id"]: e for e in state.get("emails", [])}

    failures = []

    # Check all senders are blocked and emails are read
    for eid, sender_email in spam_senders.items():
        if sender_email not in blocked_emails:
            failures.append(f"{sender_email} (from {eid}) not in blockedSenders")

        email = emails_by_id.get(eid)
        if email is None:
            failures.append(f"{eid}: not found in state")
            continue
        if email.get("isRead") is not True:
            failures.append(f"{eid}: isRead is {email.get('isRead')}, expected True")

    if failures:
        return False, "Not all spam senders blocked / emails read: " + "; ".join(failures)

    return True, "All 5 spam senders blocked and all 5 spam emails marked as read."
