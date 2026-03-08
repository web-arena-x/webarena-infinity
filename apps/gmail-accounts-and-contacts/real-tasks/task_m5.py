# Task: Move Jason Blake from other contacts to main contacts.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()
    errors = []

    other_contacts = state.get("otherContacts", [])
    still_in_other = [
        c for c in other_contacts
        if c.get("email") == "jason.blake@salesforce.com"
    ]
    if still_in_other:
        errors.append("Jason Blake (jason.blake@salesforce.com) still exists in otherContacts")

    contacts = state.get("contacts", [])
    in_main = [
        c for c in contacts
        if c.get("email") == "jason.blake@salesforce.com"
    ]
    if not in_main:
        errors.append("Jason Blake (jason.blake@salesforce.com) not found in main contacts")

    if errors:
        return False, "; ".join(errors)
    return True, "Jason Blake moved from other contacts to main contacts."
