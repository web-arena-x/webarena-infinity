import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])

    for contact in contacts:
        if (
            contact.get("firstName") == "David"
            and contact.get("lastName") == "Chen"
        ):
            if contact.get("starred") is False:
                return True, "David Chen is unstarred."
            return False, f"David Chen found but starred is {contact.get('starred')}, expected False."

    return False, "No contact found with firstName 'David', lastName 'Chen'."
