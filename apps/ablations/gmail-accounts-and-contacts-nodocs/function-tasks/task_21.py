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
        if group.get("name") == "Book Club":
            old_exists = True
        if group.get("name") == "Reading Circle":
            new_exists = True

    if old_exists:
        return False, "Contact group 'Book Club' still exists."
    if not new_exists:
        return False, "No contact group found with name 'Reading Circle'."

    return True, "'Book Club' has been renamed to 'Reading Circle'."
