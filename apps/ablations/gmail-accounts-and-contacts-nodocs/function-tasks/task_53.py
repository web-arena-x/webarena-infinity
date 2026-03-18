import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])

    for c in contacts:
        if c.get("firstName") == "Jessica" and c.get("lastName") == "Singh":
            return False, "Contact 'Jessica Singh' still exists. It should have been deleted."

    total = len(contacts)
    if total != 119:
        return False, f"Total contact count is {total}, expected 119 (was 120 before deletion)."

    return True, "Contact 'Jessica Singh' has been deleted and total contact count is 119."
