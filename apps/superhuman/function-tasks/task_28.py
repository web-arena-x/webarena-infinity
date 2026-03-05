import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    labels = state.get("labels", [])
    emails = state.get("emails", [])

    # Check that no label named 'Partnership' exists
    label_names = [l.get("name", "") for l in labels]
    if "Partnership" in label_names:
        return False, "Label 'Partnership' still exists. It should have been deleted."

    # Also check by ID that label_9 is gone
    label_ids = [l.get("id") for l in labels]
    if "label_9" in label_ids:
        return False, "Label with id 'label_9' still exists in the labels array."

    # Check that label_9 is removed from all emails' labels
    for email in emails:
        email_labels = email.get("labels", [])
        if "label_9" in email_labels:
            return False, (
                f"Email '{email.get('id')}' (subject: '{email.get('subject')}') "
                f"still has 'label_9' in its labels: {email_labels}."
            )

    return True, (
        "Label 'Partnership' (label_9) has been deleted and removed from all emails."
    )
