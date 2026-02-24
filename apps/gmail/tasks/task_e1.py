import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    for email in state.get("emails", []):
        if email.get("subject") == "Q1 Product Roadmap Review":
            if email.get("isStarred") is True:
                return True, "Task completed successfully."
            else:
                return False, f"Email 'Q1 Product Roadmap Review' found but isStarred is {email.get('isStarred')}, expected true."

    return False, "Email with subject 'Q1 Product Roadmap Review' not found."
