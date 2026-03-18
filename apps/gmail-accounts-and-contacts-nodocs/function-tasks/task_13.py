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
            if "grp_4" in groups:
                errors.append("grp_4 (Engineering Team) still in groups (should be removed)")
            if "grp_2" not in groups:
                errors.append("grp_2 (Work) no longer in groups (should be preserved)")
            if "grp_10" not in groups:
                errors.append("grp_10 (VIP) no longer in groups (should be preserved)")
            if errors:
                return False, f"Marcus Johnson found but group issues: {'; '.join(errors)}. Current groups: {groups}"
            return True, "Marcus Johnson successfully has grp_4 removed while retaining grp_2 and grp_10."

    return False, "No contact found with firstName 'Marcus' and lastName 'Johnson'."
