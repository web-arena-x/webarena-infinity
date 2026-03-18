import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])

    for contact in contacts:
        if (
            contact.get("firstName") == "Ben"
            and contact.get("lastName") == "Watkins"
        ):
            groups = contact.get("groups", [])
            if "grp_3" in groups:
                return False, f"Ben Watkins still has 'grp_3' in groups: {groups}"
            if "grp_7" not in groups:
                return False, f"Ben Watkins is missing 'grp_7' from groups: {groups}. Only 'grp_3' should have been removed."
            return True, "Ben Watkins has been removed from 'grp_3' (Friends) and still belongs to 'grp_7'."

    return False, "No contact found with firstName 'Ben', lastName 'Watkins'."
