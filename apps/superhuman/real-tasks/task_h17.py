"""Task H17: Archive all calendar invite emails in the inbox."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    target_ids = [
        "email_021", "email_022", "email_023", "email_024", "email_025",
        "email_026", "email_027", "email_028", "email_116",
    ]
    emails_by_id = {e["id"]: e for e in state.get("emails", [])}

    failures = []
    for eid in target_ids:
        email = emails_by_id.get(eid)
        if email is None:
            failures.append(f"{eid}: not found in state")
            continue
        if email.get("folder") != "done":
            failures.append(f"{eid}: folder is '{email.get('folder')}', expected 'done'")

    if failures:
        return False, "Not all calendar invite emails archived: " + "; ".join(failures)

    return True, "All 9 calendar invite inbox emails archived to done."
