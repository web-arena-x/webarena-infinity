import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    groups = state.get("contactGroups", [])
    contacts = state.get("contacts", [])

    # Check Friends label is gone
    for group in groups:
        if group.get("name") == "Friends":
            return False, "Label 'Friends' still exists in contact groups."

    # Check contacts formerly in Friends (grp_3) no longer have grp_3
    contacts_with_grp3 = [c for c in contacts if "grp_3" in c.get("groups", [])]
    if contacts_with_grp3:
        names = [f"{c.get('firstName')} {c.get('lastName')}" for c in contacts_with_grp3]
        return False, f"Contacts still have grp_3 in their groups: {', '.join(names)}"

    return True, "Label 'Friends' deleted and no contacts retain grp_3 membership."
