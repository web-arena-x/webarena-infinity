import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    groups = state.get("contactGroups", [])

    old_exists = False
    new_exists = False

    for group in groups:
        if group.get("name") == "Vendors":
            old_exists = True
        if group.get("name") == "Technology Partners":
            new_exists = True

    if old_exists:
        return False, "Contact group 'Vendors' still exists."
    if not new_exists:
        return False, "No contact group found with name 'Technology Partners'."

    return True, "'Vendors' has been renamed to 'Technology Partners'."
