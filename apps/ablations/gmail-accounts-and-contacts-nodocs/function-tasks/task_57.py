import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])

    for contact in contacts:
        if contact.get("firstName") == "Rachel" and contact.get("lastName") == "Park":
            errors = []
            if contact.get("email") != "rachel.park.personal@gmail.com":
                errors.append(f"Expected email 'rachel.park.personal@gmail.com', got '{contact.get('email')}'")
            if contact.get("notes") != "CS professor at Stanford - ML collaboration":
                errors.append(f"Expected notes 'CS professor at Stanford - ML collaboration', got '{contact.get('notes')}'")
            if errors:
                return False, "; ".join(errors)
            return True, "Rachel Park email and notes updated correctly."

    return False, "No contact found with firstName 'Rachel' and lastName 'Park'."
