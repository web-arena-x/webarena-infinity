import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify IT helpdesk promoted from Other Contacts and added to Work label."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])
    other_contacts = state.get("otherContacts", [])
    contact_groups = state.get("contactGroups", [])

    # Check IT helpdesk removed from Other Contacts
    for oc in other_contacts:
        if oc.get("email") == "it-helpdesk@techcorp.io":
            return False, (
                "IT helpdesk (it-helpdesk@techcorp.io) still in Other Contacts."
            )

    # Check IT helpdesk exists in main contacts
    helpdesk = None
    for c in contacts:
        if c.get("email") == "it-helpdesk@techcorp.io":
            helpdesk = c
            break

    if helpdesk is None:
        return False, (
            "IT helpdesk (it-helpdesk@techcorp.io) not found in main contacts."
        )

    # Check assigned to Work label
    work = None
    for g in contact_groups:
        if g.get("name") == "Work":
            work = g
            break

    if work is None:
        return False, "Work label not found."

    if work["id"] not in helpdesk.get("groups", []):
        return False, "IT helpdesk contact is not in the Work label."

    return True, (
        "IT helpdesk promoted from Other Contacts to main contacts "
        "and assigned to Work label."
    )
