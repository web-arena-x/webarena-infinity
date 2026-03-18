import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    contacts = state.get("contacts", [])
    jake = None
    for c in contacts:
        if c.get("firstName") == "Jake" and c.get("lastName") == "Morrison":
            jake = c
            break

    if jake is None:
        return False, "Contact Jake Morrison not found in contacts list."

    if jake.get("starred") is False:
        return True, "Jake Morrison is no longer starred."
    else:
        return False, f"Jake Morrison is still starred. starred={jake.get('starred')}"
