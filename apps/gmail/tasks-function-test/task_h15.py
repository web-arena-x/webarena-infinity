import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    labels = state.get("labels", [])
    emails = state.get("emails", [])

    # Check no label with name 'HR' exists
    for label in labels:
        if label.get("name") == "HR":
            return False, "Label with name 'HR' still exists."

    # Check no email has 'label_12' in labels
    for email in emails:
        email_labels = email.get("labels", [])
        if "label_12" in email_labels:
            return False, f"Email '{email.get('subject', '(no subject)')}' still has 'label_12' in its labels."

    # Find label with id 'label_11' and check its name is 'Partners'
    label_11 = None
    for label in labels:
        if label.get("id") == "label_11":
            label_11 = label
            break

    if not label_11:
        return False, "No label with id 'label_11' found."

    if label_11.get("name") != "Partners":
        return False, f"Label 'label_11' name is '{label_11.get('name')}', expected 'Partners'."

    return True, "Task completed successfully."
