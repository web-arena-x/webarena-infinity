# Task: Delete Diana Castillo.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    contacts = state.get("contacts", [])
    for contact in contacts:
        if contact.get("firstName") == "Diana" and contact.get("lastName") == "Castillo":
            return False, "Diana Castillo still exists in contacts."

    return True, "Diana Castillo has been deleted from contacts."
