"""Task H15: Remove all labels from Marcus's weekly team digest and archive it."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    emails_by_id = {e["id"]: e for e in state.get("emails", [])}
    email = emails_by_id.get("email_045")

    if email is None:
        return False, "email_045 not found in state."

    failures = []

    email_labels = email.get("labels", [])
    if email_labels != []:
        failures.append(f"labels is {email_labels}, expected []")

    if email.get("folder") != "done":
        failures.append(f"folder is '{email.get('folder')}', expected 'done'")

    if failures:
        return False, "email_045 checks failed: " + "; ".join(failures)

    return True, "email_045 (Weekly team digest): all labels removed and archived to done."
