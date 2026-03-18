import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])

    for contact in contacts:
        if contact.get("firstName") == "Natalie" and contact.get("lastName") == "Dubois":
            errors = []
            if contact.get("phone") != "+33 7 99 88 77 66":
                errors.append(f"Expected phone '+33 7 99 88 77 66', got '{contact.get('phone')}'")
            if contact.get("company") != "DesignStudio Paris":
                errors.append(f"Expected company 'DesignStudio Paris', got '{contact.get('company')}'")
            if errors:
                return False, "; ".join(errors)
            return True, "Natalie Dubois updated with phone and company correctly."

    return False, "No contact found with firstName 'Natalie' and lastName 'Dubois'."
