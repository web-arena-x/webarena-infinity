import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    emails = state.get("emails", [])
    target_subject = "Claim your $500 Amazon Gift Card"

    for email in emails:
        if email.get("subject") == target_subject:
            return False, f"Email with subject '{target_subject}' still exists and was not permanently deleted."

    return True, "Task completed successfully."
