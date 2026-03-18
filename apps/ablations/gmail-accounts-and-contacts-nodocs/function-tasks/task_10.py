import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])

    for contact in contacts:
        if contact.get("firstName") == "Mei" and contact.get("lastName") == "Zhang":
            actual_birthday = contact.get("birthday")
            if actual_birthday == "1992-07-15":
                return True, "Mei Zhang's birthday successfully updated to '1992-07-15'."
            return False, f"Mei Zhang found but birthday is '{actual_birthday}', expected '1992-07-15'."

    return False, "No contact found with firstName 'Mei' and lastName 'Zhang'."
