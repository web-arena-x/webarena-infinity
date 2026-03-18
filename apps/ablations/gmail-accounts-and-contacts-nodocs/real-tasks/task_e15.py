import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    contact_groups = state.get("contactGroups", [])
    contacts = state.get("contacts", [])

    # Check that the Investors label no longer exists
    for group in contact_groups:
        if group.get("name") == "Investors":
            return False, (
                "The 'Investors' label still exists in contactGroups. "
                "Expected it to be deleted."
            )

    # Check that no contact still references the old group ID "grp_5"
    contacts_with_old_group = []
    for contact in contacts:
        groups = contact.get("groups", [])
        if "grp_5" in groups:
            name = f"{contact.get('firstName', '')} {contact.get('lastName', '')}".strip()
            contacts_with_old_group.append(name)

    if contacts_with_old_group:
        return False, (
            f"The 'Investors' label was deleted from contactGroups, but the following "
            f"contacts still have 'grp_5' in their groups array: "
            f"{contacts_with_old_group}."
        )

    return True, (
        "The 'Investors' label has been successfully deleted and no contacts "
        "still reference the old group ID 'grp_5'."
    )
