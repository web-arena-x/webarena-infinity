import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])

    for contact in contacts:
        if contact.get("firstName") == "David" and contact.get("lastName") == "Chen":
            actual_email = contact.get("email")
            if actual_email == "david.chen.updated@gmail.com":
                return True, "David Chen's email successfully updated to 'david.chen.updated@gmail.com'."
            return False, f"David Chen found but email is '{actual_email}', expected 'david.chen.updated@gmail.com'."

    return False, "No contact found with firstName 'David' and lastName 'Chen'."
