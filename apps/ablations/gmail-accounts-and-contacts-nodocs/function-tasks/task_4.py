import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])

    for contact in contacts:
        if (
            contact.get("firstName") == "Alex"
            and contact.get("lastName") == "Demo"
            and contact.get("email") == "alex.demo@techcorp.io"
        ):
            groups = contact.get("groups", [])
            if "grp_2" in groups:
                return True, "Contact Alex Demo found with correct email and assigned to Work group (grp_2)."
            return False, f"Contact Alex Demo found but 'grp_2' not in groups: {groups}"

    return False, "No contact found with firstName 'Alex', lastName 'Demo', email 'alex.demo@techcorp.io'."
