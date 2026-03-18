import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])

    for contact in contacts:
        if contact.get("firstName") == "Tom" and contact.get("lastName") == "O'Brien":
            actual_address = contact.get("address")
            expected_address = "123 New Street, San Francisco, CA 94100"
            if actual_address == expected_address:
                return True, "Tom O'Brien's address successfully updated."
            return False, f"Tom O'Brien found but address is '{actual_address}', expected '{expected_address}'."

    return False, "No contact found with firstName 'Tom' and lastName \"O'Brien\"."
