import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])

    for contact in contacts:
        if contact.get("firstName") == "Ben" and contact.get("lastName") == "Watkins":
            errors = []
            if contact.get("company") != "Watkins Photography":
                errors.append(f"Expected company 'Watkins Photography', got '{contact.get('company')}'")
            if contact.get("jobTitle") != "Professional Photographer":
                errors.append(f"Expected jobTitle 'Professional Photographer', got '{contact.get('jobTitle')}'")
            if errors:
                return False, "; ".join(errors)
            return True, "Ben Watkins updated with company 'Watkins Photography' and jobTitle 'Professional Photographer'."

    return False, "No contact found with firstName 'Ben' and lastName 'Watkins'."
