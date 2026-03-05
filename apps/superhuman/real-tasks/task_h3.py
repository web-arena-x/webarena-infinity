"""Task H3: Mark all unread calendar emails as read."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    target_ids = ["email_021", "email_024", "email_026", "email_027"]
    emails_by_id = {e["id"]: e for e in state.get("emails", [])}

    failures = []
    for eid in target_ids:
        email = emails_by_id.get(eid)
        if email is None:
            failures.append(f"{eid}: not found in state")
            continue
        if email.get("isRead") is not True:
            failures.append(f"{eid}: isRead is {email.get('isRead')}, expected True")

    if failures:
        return False, "Not all unread calendar emails marked as read: " + "; ".join(failures)

    return True, "All unread calendar emails (email_021, email_024, email_026, email_027) marked as read."
