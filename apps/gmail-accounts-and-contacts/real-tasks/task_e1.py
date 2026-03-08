# Task: Star James O'Brien.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    contacts = state.get("contacts", [])
    for contact in contacts:
        if contact.get("firstName") == "James" and contact.get("lastName") == "O'Brien":
            if contact.get("isStarred") is True:
                return True, "James O'Brien is now starred."
            else:
                return False, f"James O'Brien found but isStarred is {contact.get('isStarred')}, expected true."

    return False, "Contact James O'Brien not found."
