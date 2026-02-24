import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    for email in state.get("emails", []):
        if email.get("subject") == "Property Listing: 45 Oak Avenue":
            if email.get("isTrashed") is True:
                return True, "Task completed successfully."
            else:
                return False, f"Email 'Property Listing: 45 Oak Avenue' found but isTrashed is {email.get('isTrashed')}, expected true."

    return False, "Email with subject 'Property Listing: 45 Oak Avenue' not found."
