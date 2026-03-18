import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])

    for contact in contacts:
        if contact.get("firstName") == "Derek" and contact.get("lastName") == "Hoffman":
            return False, "Contact Derek Hoffman still exists in contacts list."

    return True, "Contact Derek Hoffman has been deleted."
