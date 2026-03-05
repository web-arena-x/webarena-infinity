"""Task H34: Apply Partnership label to the forwarded TechCrunch feature email, set reminder for its deadline."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    # email_010 = forwarded TechCrunch feature email, deadline March 9th
    emails_by_id = {e["id"]: e for e in state.get("emails", [])}
    email = emails_by_id.get("email_010")

    if email is None:
        return False, "email_010 not found in state."

    failures = []

    email_labels = email.get("labels", [])
    if "label_9" not in email_labels:
        failures.append(f"missing Partnership label (label_9), has labels {email_labels}")

    reminder = email.get("reminder")
    if reminder is None:
        failures.append("reminder is None, expected a value")

    if failures:
        return False, "email_010 checks failed: " + "; ".join(failures)

    return True, f"email_010 (TechCrunch feature): Partnership label applied, reminder set to '{reminder}'."
