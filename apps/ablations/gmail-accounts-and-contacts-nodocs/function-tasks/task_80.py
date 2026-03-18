import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])

    for contact in contacts:
        if contact.get("firstName") == "Sophia" and contact.get("lastName") == "Andersson":
            groups = contact.get("groups", [])
            errors = []
            if "grp_2" not in groups:
                errors.append("grp_2 (Work) should be preserved but missing")
            if "grp_4" not in groups:
                errors.append("grp_4 (Engineering Team) not in groups")
            if "grp_8" not in groups:
                errors.append("grp_8 (Conference Contacts) not in groups")
            if errors:
                return False, f"Sophia Andersson group issues: {'; '.join(errors)}. Current groups: {groups}"
            return True, "Sophia Andersson added to Engineering Team and Conference Contacts (Work preserved)."

    return False, "No contact found with firstName 'Sophia' and lastName 'Andersson'."
