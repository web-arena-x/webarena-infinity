# Task: Move Tina Marshall and delete Chloe Bennett.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()
    errors = []

    other_contacts = state.get("otherContacts", [])
    contacts = state.get("contacts", [])

    # Tina Marshall should no longer be in otherContacts
    tina_in_other = [c for c in other_contacts if c.get("email") == "tina.marshall@designhub.com"]
    if tina_in_other:
        errors.append("Tina Marshall (tina.marshall@designhub.com) still exists in otherContacts")

    # Tina Marshall should be in main contacts
    tina_in_main = [c for c in contacts if c.get("email") == "tina.marshall@designhub.com"]
    if not tina_in_main:
        errors.append("Tina Marshall (tina.marshall@designhub.com) not found in main contacts")

    # Chloe Bennett should no longer be in otherContacts
    chloe_in_other = [c for c in other_contacts if c.get("email") == "chloe.b@sequoiacap.com"]
    if chloe_in_other:
        errors.append("Chloe Bennett (chloe.b@sequoiacap.com) still exists in otherContacts (should have been deleted)")

    if errors:
        return False, "; ".join(errors)
    return True, "Tina Marshall moved to main contacts and Chloe Bennett deleted from other contacts."
