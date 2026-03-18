import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])

    for contact in contacts:
        if contact.get("firstName") == "Kevin" and contact.get("lastName") == "Chen":
            errors = []
            if contact.get("company") != "Google":
                errors.append(f"Expected company 'Google', got '{contact.get('company')}'")
            if contact.get("jobTitle") != "Senior Product Manager":
                errors.append(f"Expected jobTitle 'Senior Product Manager', got '{contact.get('jobTitle')}'")
            if errors:
                return False, "; ".join(errors)
            return True, "Kevin Chen updated with company 'Google' and jobTitle 'Senior Product Manager'."

    return False, "No contact found with firstName 'Kevin' and lastName 'Chen'."
