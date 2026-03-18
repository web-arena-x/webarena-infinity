import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])

    for contact in contacts:
        if contact.get("firstName") == "TestContact" and not contact.get("lastName") and not contact.get("email"):
            return True, "Contact with only firstName 'TestContact' found (no lastName, no email)."

    return False, "No contact found with firstName 'TestContact' and empty lastName/email."
