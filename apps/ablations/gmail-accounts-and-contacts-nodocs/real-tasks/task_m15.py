import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    target_email = "mike.sales@hubspot.com"

    # Check that the contact is no longer in otherContacts
    other_contacts = state.get("otherContacts", [])
    still_in_other = False
    for oc in other_contacts:
        if oc.get("email") == target_email:
            still_in_other = True
            break

    # Check that the contact now exists in main contacts
    contacts = state.get("contacts", [])
    in_contacts = False
    for c in contacts:
        if c.get("email") == target_email:
            in_contacts = True
            break

    errors = []

    if still_in_other:
        errors.append(f"'{target_email}' is still present in Other Contacts.")

    if not in_contacts:
        errors.append(f"'{target_email}' was not found in the main contacts list.")

    if errors:
        return False, " ".join(errors)

    return True, f"HubSpot contact '{target_email}' has been moved from Other Contacts to the main contacts list."
