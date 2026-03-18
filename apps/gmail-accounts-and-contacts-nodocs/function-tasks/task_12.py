import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])

    for contact in contacts:
        if contact.get("firstName") == "Nina" and contact.get("lastName") == "Patel":
            groups = contact.get("groups", [])
            errors = []
            if "grp_10" not in groups:
                errors.append("grp_10 (VIP) not found in groups")
            if "grp_2" not in groups:
                errors.append("grp_2 (Work) no longer in groups (should be preserved)")
            if "grp_4" not in groups:
                errors.append("grp_4 (Engineering Team) no longer in groups (should be preserved)")
            if errors:
                return False, f"Nina Patel found but group issues: {'; '.join(errors)}. Current groups: {groups}"
            return True, "Nina Patel successfully has grp_10 (VIP) added while retaining grp_2 and grp_4."

    return False, "No contact found with firstName 'Nina' and lastName 'Patel'."
