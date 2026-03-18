import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])

    for contact in contacts:
        if contact.get("firstName") == "Emma" and contact.get("lastName") == "Thompson":
            return False, "Contact Emma Thompson still exists in contacts (should have been deleted)."

    return True, "Contact Emma Thompson successfully deleted (not found in contacts)."
