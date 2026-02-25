import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    labels = state.get("labels", [])
    for label in labels:
        if label.get("name") == "Newsletters":
            return False, "Label 'Newsletters' still exists in labels."

    for email in state.get("emails", []):
        email_labels = email.get("labels", [])
        if "label_6" in email_labels:
            return False, f"Email '{email.get('subject', '(no subject)')}' still has 'label_6' in its labels."

    return True, "Task completed successfully."
