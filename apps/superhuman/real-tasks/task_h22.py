"""Task H22: Mark the v2 API beta feedback thread as read, add Project Alpha label, set reminder for tomorrow."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    emails_by_id = {e["id"]: e for e in state.get("emails", [])}
    email = emails_by_id.get("email_114")

    if email is None:
        return False, "email_114 not found in state."

    failures = []

    if email.get("isRead") is not True:
        failures.append(f"isRead is {email.get('isRead')}, expected True")

    email_labels = email.get("labels", [])
    if "label_1" not in email_labels:
        failures.append(f"missing Project Alpha label (label_1), has labels {email_labels}")

    reminder = email.get("reminder")
    if reminder is None:
        failures.append("reminder is None, expected a value")

    if failures:
        return False, "email_114 checks failed: " + "; ".join(failures)

    return True, f"email_114: marked read, Project Alpha label applied, reminder set to '{reminder}'."
