import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])

    natalie = None
    for c in contacts:
        if c.get("firstName") == "Natalie" and c.get("lastName") == "Dubois":
            natalie = c
            break

    if natalie is None:
        return False, "Contact 'Natalie Dubois' not found."

    groups = natalie.get("groups", [])

    if "grp_2" not in groups:
        return False, f"Contact 'Natalie Dubois' does not have 'grp_2' (Work) in groups. Current groups: {groups}"

    if "grp_10" not in groups:
        return False, f"Contact 'Natalie Dubois' does not have 'grp_10' (VIP) in groups. Current groups: {groups}"

    return True, "Contact 'Natalie Dubois' has both 'grp_2' (Work) and 'grp_10' (VIP) in her groups."
