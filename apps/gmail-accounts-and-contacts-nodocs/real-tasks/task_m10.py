import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])

    # Find Alex Martinez
    alex = None
    for c in contacts:
        if c.get("firstName") == "Alex" and c.get("lastName") == "Martinez":
            alex = c
            break

    if not alex:
        return False, "Contact with firstName='Alex' and lastName='Martinez' not found."

    # Verify phone
    if alex.get("phone") != "+1 (415) 555-1100":
        return False, f"Expected phone '+1 (415) 555-1100', got '{alex.get('phone')}'."

    # Verify birthday
    if alex.get("birthday") != "1994-01-20":
        return False, f"Expected birthday '1994-01-20', got '{alex.get('birthday')}'."

    return True, "Alex Martinez's phone updated to '+1 (415) 555-1100' and birthday set to '1994-01-20'."
