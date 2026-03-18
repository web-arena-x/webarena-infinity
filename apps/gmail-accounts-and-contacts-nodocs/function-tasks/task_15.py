import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])

    for contact in contacts:
        if (
            contact.get("firstName") == "Timothy"
            and contact.get("lastName") == "Buchanan"
        ):
            return False, "Contact Timothy Buchanan still exists."

    return True, "Contact Timothy Buchanan has been deleted."
