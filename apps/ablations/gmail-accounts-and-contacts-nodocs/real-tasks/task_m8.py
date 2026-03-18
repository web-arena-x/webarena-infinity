import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])

    # Find Natalie Dubois
    natalie = None
    for c in contacts:
        if c.get("firstName") == "Natalie" and c.get("lastName") == "Dubois":
            natalie = c
            break

    if not natalie:
        return False, "Contact with firstName='Natalie' and lastName='Dubois' not found."

    # Find Work group
    contact_groups = state.get("contactGroups", [])
    work_group = None
    friends_group = None
    for g in contact_groups:
        if g.get("name") == "Work":
            work_group = g
        if g.get("name") == "Friends":
            friends_group = g

    if not work_group:
        return False, "Contact group 'Work' not found in contactGroups."
    if not friends_group:
        return False, "Contact group 'Friends' not found in contactGroups."

    work_id = work_group.get("id")
    friends_id = friends_group.get("id")
    natalie_groups = natalie.get("groups", [])

    if work_id not in natalie_groups:
        return False, f"Work group ID '{work_id}' not found in Natalie Dubois's groups: {natalie_groups}."

    if friends_id not in natalie_groups:
        return False, f"Friends group ID '{friends_id}' not found in Natalie Dubois's groups: {natalie_groups}."

    return True, "Natalie Dubois successfully moved into both Work and Friends labels."
