"""Task H39: Move every email in the trash back to the inbox and unblock all blocked senders."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    failures = []

    # Trash emails in seed: email_104, 105, 106, 107, 108 — should all be inbox now
    trash_ids = ["email_104", "email_105", "email_106", "email_107", "email_108"]
    emails_by_id = {e["id"]: e for e in state.get("emails", [])}

    for eid in trash_ids:
        email = emails_by_id.get(eid)
        if email is None:
            failures.append(f"{eid}: not found in state")
            continue
        if email.get("folder") != "inbox":
            failures.append(f"{eid}: folder is '{email.get('folder')}', expected 'inbox'")

    # Blocked senders should be empty
    blocked = state.get("blockedSenders", [])
    if len(blocked) > 0:
        blocked_emails = [s.get("email", str(s)) for s in blocked]
        failures.append(f"blockedSenders not empty: {blocked_emails}")

    if failures:
        return False, "Trash/unblock checks failed: " + "; ".join(failures)

    return True, "All 5 trash emails moved to inbox and all blocked senders removed."
