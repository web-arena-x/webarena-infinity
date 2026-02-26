import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    emails = state.get("emails", [])
    target_subject = "Quarterly Team Dinner"

    for email in emails:
        if email.get("subject") == target_subject:
            if email.get("isMuted") is True:
                return True, "Task completed successfully."
            else:
                return False, f"Email '{target_subject}' is not muted (isMuted={email.get('isMuted')})."

    return False, f"Email with subject '{target_subject}' not found."
