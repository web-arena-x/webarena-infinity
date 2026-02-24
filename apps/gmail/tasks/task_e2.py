import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    for email in state.get("emails", []):
        if email.get("subject") == "Design System Update v4.2":
            if email.get("isRead") is True:
                return True, "Task completed successfully."
            else:
                return False, f"Email 'Design System Update v4.2' found but isRead is {email.get('isRead')}, expected true."

    return False, "Email with subject 'Design System Update v4.2' not found."
