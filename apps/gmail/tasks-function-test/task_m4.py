import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    emails = state.get("emails", [])
    target_email = None
    for email in emails:
        if email.get("subject") == "Strategy Workshop Follow-up":
            target_email = email
            break

    if not target_email:
        return False, "Could not find email with subject 'Strategy Workshop Follow-up'."

    labels = target_email.get("labels", [])
    if "label_10" in labels:
        return True, "Task completed successfully."

    return False, (
        f"Email 'Strategy Workshop Follow-up' does not have 'label_10' (Meetings) "
        f"in its labels. Current labels: {labels}"
    )
