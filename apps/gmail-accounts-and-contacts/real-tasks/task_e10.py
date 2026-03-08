# Task: Unstar Emily Rodriguez.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    contacts = state.get("contacts", [])
    for contact in contacts:
        if contact.get("firstName") == "Emily" and contact.get("lastName") == "Rodriguez":
            if contact.get("isStarred") is False:
                return True, "Emily Rodriguez is now unstarred."
            else:
                return False, f"Emily Rodriguez isStarred is {contact.get('isStarred')}, expected false."

    return False, "Contact Emily Rodriguez not found."
