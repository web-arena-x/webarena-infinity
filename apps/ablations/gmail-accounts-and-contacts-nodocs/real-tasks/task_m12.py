import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find the "Open Source" contact group
    contact_groups = state.get("contactGroups", [])
    open_source_group = None
    for g in contact_groups:
        if g.get("name") == "Open Source":
            open_source_group = g
            break

    if open_source_group is None:
        return False, "Contact group 'Open Source' not found."

    group_id = open_source_group.get("id")

    # Find Philip Okonkwo
    contacts = state.get("contacts", [])
    philip = None
    damian = None
    for c in contacts:
        if c.get("firstName") == "Philip" and c.get("lastName") == "Okonkwo":
            philip = c
        if c.get("firstName") == "Damian" and c.get("lastName") == "Kowalczyk":
            damian = c

    errors = []

    if philip is None:
        errors.append("Contact Philip Okonkwo not found.")
    elif group_id not in philip.get("groups", []):
        errors.append(
            f"Philip Okonkwo does not have group '{group_id}' (Open Source) in groups. "
            f"Current groups: {philip.get('groups', [])}."
        )

    if damian is None:
        errors.append("Contact Damian Kowalczyk not found.")
    elif group_id not in damian.get("groups", []):
        errors.append(
            f"Damian Kowalczyk does not have group '{group_id}' (Open Source) in groups. "
            f"Current groups: {damian.get('groups', [])}."
        )

    if errors:
        return False, " ".join(errors)

    return True, "Contact group 'Open Source' exists and both Philip Okonkwo and Damian Kowalczyk are members."
