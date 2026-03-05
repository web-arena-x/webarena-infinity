"""Task H19: Unstar outage email, remove all labels, archive it."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    emails_by_id = {e["id"]: e for e in state.get("emails", [])}
    email = emails_by_id.get("email_004")

    if email is None:
        return False, "email_004 not found in state."

    failures = []

    if email.get("isStarred") is not False:
        failures.append(f"isStarred is {email.get('isStarred')}, expected False")

    email_labels = email.get("labels", [])
    if email_labels != []:
        failures.append(f"labels is {email_labels}, expected []")

    if email.get("folder") != "done":
        failures.append(f"folder is '{email.get('folder')}', expected 'done'")

    if failures:
        return False, "email_004 checks failed: " + "; ".join(failures)

    return True, "email_004 (outage email): unstarred, all labels removed, archived to done."
