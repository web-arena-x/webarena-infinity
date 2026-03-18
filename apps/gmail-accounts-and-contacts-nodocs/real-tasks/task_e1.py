import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    contacts = state.get("contacts", [])
    mei = None
    for c in contacts:
        if c.get("firstName") == "Mei" and c.get("lastName") == "Zhang":
            mei = c
            break

    if mei is None:
        return False, "Contact Mei Zhang not found in contacts list."

    if mei.get("starred") is True:
        return True, "Mei Zhang is starred."
    else:
        return False, f"Mei Zhang is not starred. starred={mei.get('starred')}"
