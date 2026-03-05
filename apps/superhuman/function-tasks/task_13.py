import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    emails = state.get("emails", [])

    target_subject = "Re: Re: v2 API beta feedback"
    email = next((e for e in emails if target_subject in e.get("subject", "")), None)

    if email is None:
        return False, f"Could not find email with subject containing '{target_subject}'."

    labels = email.get("labels", [])
    missing = []
    if "label_1" not in labels:
        missing.append("label_1 (Project Alpha)")
    if "label_2" not in labels:
        missing.append("label_2 (Q1 Planning)")

    if missing:
        return False, f"Email '{target_subject}' labels are {labels}, missing: {', '.join(missing)}."

    return True, f"Email '{target_subject}' has both 'Project Alpha' (label_1) and 'Q1 Planning' (label_2) labels."
