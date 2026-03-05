"""Task H37: Archive every unread email in the Other split of the inbox."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    # Unread inbox emails with split='other' in seed state:
    # email_029, 030, 033, 042, 118, 122
    target_ids = ["email_029", "email_030", "email_033", "email_042",
                  "email_118", "email_122"]

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
        return False, "Not all unread Other emails archived: " + "; ".join(failures)

    return True, "All 6 unread Other-split inbox emails archived to Done."
