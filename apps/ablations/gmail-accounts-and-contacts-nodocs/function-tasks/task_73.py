import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])

    for contact in contacts:
        if (
            contact.get("firstName") == "Multi"
            and contact.get("lastName") == "Label"
            and contact.get("email") == "multi.label@test.com"
        ):
            groups = contact.get("groups", [])
            errors = []
            if "grp_2" not in groups:
                errors.append("grp_2 (Work) not in groups")
            if "grp_4" not in groups:
                errors.append("grp_4 (Engineering Team) not in groups")
            if "grp_10" not in groups:
                errors.append("grp_10 (VIP) not in groups")
            if errors:
                return False, f"Contact found but missing labels: {'; '.join(errors)}. Current groups: {groups}"
            return True, "Contact 'Multi Label' created with Work, Engineering Team, and VIP labels."

    return False, "No contact found with firstName 'Multi', lastName 'Label', email 'multi.label@test.com'."
