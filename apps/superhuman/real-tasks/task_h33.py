"""Task H33: Cancel the scheduled email addressed to the QuantumLeap contact."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    # email_102 = scheduled follow-up to QuantumLeap AI
    emails_by_id = {e["id"]: e for e in state.get("emails", [])}
    email = emails_by_id.get("email_102")

    if email is None:
        return False, "email_102 not found in state."

    failures = []

    if email.get("isScheduled") is not False:
        failures.append(f"isScheduled is {email.get('isScheduled')}, expected False")

    if email.get("isDraft") is not True:
        failures.append(f"isDraft is {email.get('isDraft')}, expected True")

    if failures:
        return False, "email_102 cancel checks failed: " + "; ".join(failures)

    return True, "email_102 (QuantumLeap follow-up) cancelled and converted to draft."
