import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    contacts = state.get("contacts", [])
    for c in contacts:
        if c.get("firstName") == "Penny" and c.get("lastName") == "Crawford":
            return False, "Contact Penny Crawford still exists in the contacts list."

    return True, "Contact Penny Crawford has been successfully deleted."
