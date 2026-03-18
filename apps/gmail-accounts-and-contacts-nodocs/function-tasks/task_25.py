import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    groups = state.get("contactGroups", [])

    for group in groups:
        if group.get("name") == "Conference Contacts":
            return False, "Contact group 'Conference Contacts' still exists."

    return True, "Contact group 'Conference Contacts' has been deleted."
