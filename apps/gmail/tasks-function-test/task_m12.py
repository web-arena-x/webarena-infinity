import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    emails = state.get("emails", [])
    target_email = None
    for email in emails:
        if email.get("subject") == "Lab Tour Invitation":
            target_email = email
            break

    if not target_email:
        return False, "Could not find email with subject 'Lab Tour Invitation'."

    labels = target_email.get("labels", [])
    errors = []
    if "label_8" not in labels:
        errors.append("'label_8' (Education) not in labels")
    if "label_19" not in labels:
        errors.append("'label_19' (Reference) not in labels")

    if errors:
        return False, (
            f"Email 'Lab Tour Invitation': {'; '.join(errors)}. "
            f"Current labels: {labels}"
        )

    return True, "Task completed successfully."
