import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])

    for contact in contacts:
        if (
            contact.get("firstName") == "Maria"
            and contact.get("lastName") == "Lopez"
            and contact.get("email") == "maria.lopez@example.com"
        ):
            return True, "Contact Maria Lopez with correct email found."

    return False, "No contact found with firstName 'Maria', lastName 'Lopez', email 'maria.lopez@example.com'."
