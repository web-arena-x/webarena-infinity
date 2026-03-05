"""Task H30: Find the email mentioning a competing offer expiring March 20th and add the Urgent label."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    # email_005 from Laura Hendricks mentions Kevin Zhao's competing offer expiring March 20th
    emails_by_id = {e["id"]: e for e in state.get("emails", [])}
    email = emails_by_id.get("email_005")

    if email is None:
        return False, "email_005 not found in state."

    email_labels = email.get("labels", [])
    if "label_7" not in email_labels:
        return False, f"email_005 missing Urgent label (label_7), has labels {email_labels}."

    return True, "email_005 (candidate feedback with competing offer) has Urgent label applied."
