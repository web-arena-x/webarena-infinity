import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    emails = state.get("emails", [])

    target_email = None
    for email in emails:
        if email.get("subject") == "CI/CD Pipeline Migration Plan":
            target_email = email
            break

    if not target_email:
        return False, "No email found with subject 'CI/CD Pipeline Migration Plan'."

    if target_email.get("isSnoozed") is not True:
        return False, f"Email isSnoozed is {target_email.get('isSnoozed')}, expected True."

    if target_email.get("snoozeUntil") is None:
        return False, "Email snoozeUntil is None, expected a value."

    email_labels = target_email.get("labels", [])
    if "label_17" in email_labels:
        return False, f"Email still has 'label_17' (Action Required) in its labels: {email_labels}"

    return True, "Task completed successfully."
