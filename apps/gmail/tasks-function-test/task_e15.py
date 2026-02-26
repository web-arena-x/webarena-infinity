import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    emails = state.get("emails", [])
    target_substring = "Congratulations! You won $10,000!"

    for email in emails:
        subject = email.get("subject", "")
        if target_substring in subject:
            return False, f"Email with subject containing '{target_substring}' still exists and was not permanently deleted."

    return True, "Task completed successfully."
