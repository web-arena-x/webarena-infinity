import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    emails = state.get("emails", [])
    target_subject = "Contract Review: Vendor Agreement"

    for email in emails:
        if email.get("subject") == target_subject:
            is_important = email.get("isImportant", False)
            labels = email.get("labels", [])

            if is_important:
                return False, f"Email '{target_subject}' is still marked as important (isImportant=True)."
            if "IMPORTANT" in labels:
                return False, f"Email '{target_subject}' still has 'IMPORTANT' label. Current labels: {labels}."
            return True, "Task completed successfully."

    return False, f"Email with subject '{target_subject}' not found."
