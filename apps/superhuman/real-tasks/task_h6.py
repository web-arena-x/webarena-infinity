"""Task H6: Move all emails labeled Urgent to Done."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    target_ids = ["email_004", "email_009", "email_012", "email_014", "email_019", "email_125"]
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
        return False, "Not all Urgent-labeled emails moved to Done: " + "; ".join(failures)

    return True, "All 6 Urgent-labeled emails moved to Done."
