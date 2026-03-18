import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Update the phone number for Coastal Cafe Group to +64 3 441 9999."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    contacts = state.get("contacts", [])

    target = None
    for contact in contacts:
        if contact.get("name") == "Coastal Cafe Group":
            target = contact
            break

    if target is None:
        return False, "Contact 'Coastal Cafe Group' not found"

    phone = target.get("phone")
    if phone == "+64 3 441 9999":
        return True, "Coastal Cafe Group phone has been updated to '+64 3 441 9999'"
    else:
        return False, f"Coastal Cafe Group phone is '{phone}', expected '+64 3 441 9999'"
