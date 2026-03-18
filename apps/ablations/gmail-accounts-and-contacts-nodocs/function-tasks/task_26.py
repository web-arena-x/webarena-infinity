import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    other_contacts = state.get("otherContacts", [])
    contacts = state.get("contacts", [])

    still_in_other = False
    in_main = False

    for oc in other_contacts:
        if oc.get("email") == "jason.recruiter@linkedin.com":
            still_in_other = True

    for contact in contacts:
        if contact.get("email") == "jason.recruiter@linkedin.com":
            in_main = True

    if still_in_other:
        return False, "Other contact with email 'jason.recruiter@linkedin.com' still exists in other contacts."
    if not in_main:
        return False, "No contact with email 'jason.recruiter@linkedin.com' found in main contacts."

    return True, "Other contact 'jason.recruiter@linkedin.com' has been promoted to main contacts."
