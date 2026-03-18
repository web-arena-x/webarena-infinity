import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    groups = state.get("contactGroups", [])

    for group in groups:
        if group.get("name") == "Emergency Contacts":
            return True, "Contact group 'Emergency Contacts' exists."

    return False, "No contact group found with name 'Emergency Contacts'."
