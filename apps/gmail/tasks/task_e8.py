import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    for email in state.get("emails", []):
        if email.get("subject") == "Your recommendations: Tech deals of the week":
            if email.get("isSpam") is True:
                return True, "Task completed successfully."
            else:
                return False, f"Email 'Your recommendations: Tech deals of the week' found but isSpam is {email.get('isSpam')}, expected true."

    return False, "Email with subject 'Your recommendations: Tech deals of the week' not found."
