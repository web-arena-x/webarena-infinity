import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Change the email address for Ridgeway University to billing@ridgewayuni.ac.nz."""
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
        if contact.get("name") == "Ridgeway University":
            target = contact
            break

    if target is None:
        return False, "Contact 'Ridgeway University' not found"

    email = target.get("email")
    if email == "billing@ridgewayuni.ac.nz":
        return True, "Ridgeway University email has been updated to 'billing@ridgewayuni.ac.nz'"
    else:
        return False, f"Ridgeway University email is '{email}', expected 'billing@ridgewayuni.ac.nz'"
