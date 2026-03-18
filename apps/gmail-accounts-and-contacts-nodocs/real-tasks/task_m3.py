import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    target_email = "jason.recruiter@linkedin.com"

    # Verify the contact is no longer in otherContacts
    other_contacts = state.get("otherContacts", [])
    for oc in other_contacts:
        if oc.get("email") == target_email:
            return False, f"Contact with email '{target_email}' still exists in otherContacts."

    # Verify the contact now exists in contacts
    contacts = state.get("contacts", [])
    found = False
    for c in contacts:
        if c.get("email") == target_email:
            found = True
            break

    if not found:
        return False, f"Contact with email '{target_email}' not found in main contacts list."

    return True, f"LinkedIn recruiter ({target_email}) successfully promoted from Other Contacts to main contacts."
