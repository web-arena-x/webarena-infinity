import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])

    for contact in contacts:
        if (
            contact.get("firstName") == "Alex"
            and contact.get("lastName") == "Martinez"
        ):
            if contact.get("starred") is True:
                return True, "Alex Martinez is starred."
            return False, f"Alex Martinez found but starred is {contact.get('starred')}, expected True."

    return False, "No contact found with firstName 'Alex', lastName 'Martinez'."
