import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])

    for contact in contacts:
        if contact.get("firstName") == "Marcus" and contact.get("lastName") == "Johnson":
            groups = contact.get("groups", [])
            errors = []
            if "grp_5" not in groups:
                errors.append("grp_5 (Investors) not in groups")
            if "grp_2" not in groups:
                errors.append("grp_2 (Work) should be preserved but missing")
            if "grp_4" not in groups:
                errors.append("grp_4 (Engineering Team) should be preserved but missing")
            if "grp_10" not in groups:
                errors.append("grp_10 (VIP) should be preserved but missing")
            if errors:
                return False, f"Marcus Johnson group issues: {'; '.join(errors)}. Current groups: {groups}"
            return True, "Marcus Johnson added to Investors while retaining Work, Engineering Team, and VIP."

    return False, "No contact found with firstName 'Marcus' and lastName 'Johnson'."
