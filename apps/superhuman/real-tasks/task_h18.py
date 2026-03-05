"""Task H18: Delete all emails in the trash and mark every spam email as read."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    emails = state.get("emails", [])
    failures = []

    # Check no emails remain in trash
    trash_emails = [e for e in emails if e.get("folder") == "trash"]
    if trash_emails:
        trash_ids = [e["id"] for e in trash_emails]
        failures.append(f"Trash still has {len(trash_emails)} email(s): {trash_ids}")

    # Check all spam emails are read
    spam_emails = [e for e in emails if e.get("folder") == "spam"]
    for email in spam_emails:
        if email.get("isRead") is not True:
            failures.append(f"{email['id']}: spam email isRead is {email.get('isRead')}, expected True")

    if failures:
        return False, "Trash/spam checks failed: " + "; ".join(failures)

    return True, "All trash emails deleted and all spam emails marked as read."
