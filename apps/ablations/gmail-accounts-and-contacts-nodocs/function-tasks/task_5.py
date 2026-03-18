import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])

    for contact in contacts:
        if (
            contact.get("firstName") == "Jane"
            and contact.get("lastName") == "Test"
            and contact.get("email") == "jane.test@gmail.com"
        ):
            groups = contact.get("groups", [])
            missing = []
            if "grp_1" not in groups:
                missing.append("grp_1 (Family)")
            if "grp_3" not in groups:
                missing.append("grp_3 (Friends)")
            if missing:
                return False, f"Contact Jane Test found but missing groups: {', '.join(missing)}. Current groups: {groups}"
            return True, "Contact Jane Test found with correct email and assigned to both Family (grp_1) and Friends (grp_3)."

    return False, "No contact found with firstName 'Jane', lastName 'Test', email 'jane.test@gmail.com'."
