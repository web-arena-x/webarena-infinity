import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])

    for contact in contacts:
        if contact.get("firstName") == "Amy" and contact.get("lastName") == "Chen-Wu":
            actual_phone = contact.get("phone")
            if actual_phone == "+1 (510) 555-9999":
                return True, "Amy Chen-Wu's phone successfully updated to '+1 (510) 555-9999'."
            return False, f"Amy Chen-Wu found but phone is '{actual_phone}', expected '+1 (510) 555-9999'."

    return False, "No contact found with firstName 'Amy' and lastName 'Chen-Wu'."
