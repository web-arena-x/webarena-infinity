import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    emails = state.get("emails", [])

    target_subject = "Urgent: Production outage"
    email = next((e for e in emails if target_subject in e.get("subject", "")), None)

    if email is None:
        return False, f"Could not find email with subject containing '{target_subject}'."

    labels = email.get("labels", [])
    if "label_7" in labels:
        return False, f"Email '{target_subject}' still has 'label_7' (Urgent) in labels {labels}, expected it removed."

    return True, f"Email '{target_subject}' no longer has the 'Urgent' label (label_7)."
