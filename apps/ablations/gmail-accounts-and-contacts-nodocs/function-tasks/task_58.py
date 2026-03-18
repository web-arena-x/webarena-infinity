import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])

    for contact in contacts:
        if contact.get("firstName") == "Tom" and contact.get("lastName") == "O'Brien":
            birthday = contact.get("birthday", "")
            if birthday == "" or birthday is None:
                return True, "Tom O'Brien's birthday has been cleared."
            return False, f"Tom O'Brien's birthday is still set to '{birthday}', expected empty."

    return False, "No contact found with firstName 'Tom' and lastName \"O'Brien\"."
