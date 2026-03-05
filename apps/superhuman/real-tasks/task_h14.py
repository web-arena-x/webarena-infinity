"""Task H14: Star Kevin Zhao's partnership inquiry, apply Urgent label, set reminder for tomorrow."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    emails_by_id = {e["id"]: e for e in state.get("emails", [])}
    email = emails_by_id.get("email_007")

    if email is None:
        return False, "email_007 not found in state."

    failures = []

    if email.get("isStarred") is not True:
        failures.append(f"isStarred is {email.get('isStarred')}, expected True")

    email_labels = email.get("labels", [])
    if "label_7" not in email_labels:
        failures.append(f"missing Urgent label (label_7), has labels {email_labels}")

    reminder = email.get("reminder")
    if reminder is None:
        failures.append("reminder is None, expected a value")

    if failures:
        return False, "email_007 checks failed: " + "; ".join(failures)

    return True, f"email_007: starred, Urgent label applied, reminder set to '{reminder}'."
