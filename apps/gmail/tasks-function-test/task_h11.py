import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    emails = state.get("emails", [])

    target_email = None
    for email in emails:
        subject = email.get("subject", "")
        if "Tech deals of the week" in subject:
            target_email = email
            break

    if not target_email:
        return False, "No email found with subject containing 'Tech deals of the week'."

    category = (target_email.get("category") or "").lower()
    if category != "primary":
        return False, f"Email category is '{target_email.get('category')}', expected 'primary'."

    email_labels = target_email.get("labels", [])

    if "CATEGORY_PRIMARY" not in email_labels:
        return False, f"Email does not have 'CATEGORY_PRIMARY' in its labels: {email_labels}"

    if "CATEGORY_PROMOTIONS" in email_labels:
        return False, f"Email still has 'CATEGORY_PROMOTIONS' in its labels: {email_labels}"

    if "label_17" not in email_labels:
        return False, f"Email does not have 'label_17' (Action Required) in its labels: {email_labels}"

    return True, "Task completed successfully."
