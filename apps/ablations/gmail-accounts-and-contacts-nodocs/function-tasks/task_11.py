import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])

    expected_notes = "Design system owner - working on v2 redesign"

    for contact in contacts:
        if contact.get("firstName") == "Lisa" and contact.get("lastName") == "Kim":
            actual_notes = contact.get("notes")
            if actual_notes == expected_notes:
                return True, "Lisa Kim's notes successfully updated."
            return False, f"Lisa Kim found but notes is '{actual_notes}', expected '{expected_notes}'."

    return False, "No contact found with firstName 'Lisa' and lastName 'Kim'."
