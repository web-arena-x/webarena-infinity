import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    for email in state.get("emails", []):
        if email.get("subject") == "Partnership Opportunity - Series B Company":
            if email.get("isStarred") is False:
                return True, "Task completed successfully."
            else:
                return False, f"Email found but isStarred is {email.get('isStarred')}, expected false."

    return False, "Email with subject 'Partnership Opportunity - Series B Company' not found."
