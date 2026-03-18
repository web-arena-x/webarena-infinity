import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find the new contact
    contacts = state.get("contacts", [])
    elena = None
    for c in contacts:
        if c.get("firstName") == "Elena" and c.get("lastName") == "Vasquez":
            elena = c
            break

    if elena is None:
        return False, "Contact Elena Vasquez not found in contacts list."

    errors = []

    if elena.get("email") != "elena.vasquez@greentech.io":
        errors.append(
            f"Expected email='elena.vasquez@greentech.io', got '{elena.get('email')}'."
        )

    if elena.get("company") != "GreenTech Solutions":
        errors.append(
            f"Expected company='GreenTech Solutions', got '{elena.get('company')}'."
        )

    if elena.get("jobTitle") != "Sustainability Director":
        errors.append(
            f"Expected jobTitle='Sustainability Director', got '{elena.get('jobTitle')}'."
        )

    # Find Conference Contacts group
    contact_groups = state.get("contactGroups", [])
    conf_group = None
    for g in contact_groups:
        if g.get("name") == "Conference Contacts":
            conf_group = g
            break

    if conf_group is None:
        # The group may have been renamed; search by original id grp_8
        # But we should check by name first as the task says "Conference Contacts label"
        errors.append("Contact group 'Conference Contacts' not found.")
    else:
        conf_group_id = conf_group.get("id")
        if conf_group_id not in elena.get("groups", []):
            errors.append(
                f"Elena Vasquez is not assigned to 'Conference Contacts' (group id '{conf_group_id}'). "
                f"Current groups: {elena.get('groups', [])}."
            )

    if errors:
        return False, " ".join(errors)

    return True, "Contact Elena Vasquez created with correct details and assigned to Conference Contacts."
