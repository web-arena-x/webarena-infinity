import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])

    expected = {
        "firstName": "John",
        "lastName": "Doe",
        "email": "john.doe@example.com",
        "phone": "+1 (555) 999-0001",
        "company": "Acme Corp",
        "jobTitle": "CEO",
        "address": "123 Main St, Springfield, IL 62701",
        "birthday": "1990-01-15",
        "notes": "Test contact with all fields",
    }

    for contact in contacts:
        if contact.get("firstName") == "John" and contact.get("lastName") == "Doe":
            mismatches = []
            for key, value in expected.items():
                actual = contact.get(key)
                if actual != value:
                    mismatches.append(f"{key}: expected '{value}', got '{actual}'")
            if mismatches:
                return False, "Contact John Doe found but fields mismatch: " + "; ".join(mismatches)
            return True, "Contact John Doe found with all fields matching."

    return False, "No contact found with firstName 'John' and lastName 'Doe'."
