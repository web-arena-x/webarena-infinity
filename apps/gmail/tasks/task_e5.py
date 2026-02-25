import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    for email in state.get("emails", []):
        if email.get("subject") == "CI/CD Pipeline Migration Plan":
            is_important = email.get("isImportant", False)
            labels = email.get("labels", [])
            has_important_label = "IMPORTANT" in labels

            if is_important and has_important_label:
                return True, "Task completed successfully."
            else:
                return False, f"Email found but isImportant={is_important}, 'IMPORTANT' in labels={has_important_label}."

    return False, "Email with subject 'CI/CD Pipeline Migration Plan' not found."
