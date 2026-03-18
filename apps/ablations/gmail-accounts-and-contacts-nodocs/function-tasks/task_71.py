import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])
    other_contacts = state.get("otherContacts", [])

    # Check promoted to main contacts
    found_in_main = any(c.get("email") == "billing@aws.amazon.com" for c in contacts)
    if not found_in_main:
        return False, "Contact 'billing@aws.amazon.com' not found in main contacts."

    # Check removed from other contacts
    still_in_other = any(oc.get("email") == "billing@aws.amazon.com" for oc in other_contacts)
    if still_in_other:
        return False, "Contact 'billing@aws.amazon.com' still exists in Other Contacts."

    return True, "Contact 'billing@aws.amazon.com' promoted to main contacts successfully."
