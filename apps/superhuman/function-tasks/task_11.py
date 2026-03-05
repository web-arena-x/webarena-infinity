import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    emails = state.get("emails", [])

    target_subject = "Re: Board deck"
    email = next((e for e in emails if target_subject in e.get("subject", "")), None)

    if email is None:
        return False, f"Could not find email with subject containing '{target_subject}'."

    labels = email.get("labels", [])
    if "label_10" not in labels:
        return False, f"Email '{target_subject}' labels are {labels}, expected 'label_10' (Engineering) to be present."

    return True, f"Email '{target_subject}' has the 'Engineering' label (label_10)."
