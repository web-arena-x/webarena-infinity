# Task: Unstar all starred except Family.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()
    errors = []

    contacts = state.get("contacts", [])
    contact_map = {}
    for c in contacts:
        full_name = f"{c.get('firstName', '')} {c.get('lastName', '')}".strip()
        contact_map[full_name] = c

    # Family contacts should remain starred
    should_be_starred = [
        "Margaret Johnson",
        "Richard Johnson",
        "Laura Johnson-Martinez",
    ]
    for name in should_be_starred:
        contact = contact_map.get(name)
        if contact is None:
            errors.append(f"Contact '{name}' not found")
        elif not contact.get("isStarred"):
            errors.append(f"'{name}' (Family) should still be starred but is not")

    # Non-family previously-starred contacts should be unstarred
    should_be_unstarred = [
        "Sarah Chen",
        "Marcus Williams",
        "Emily Rodriguez",
        "Priya Sharma",
        "Kevin Zhao",
        "Maya Patel",
        "Jake Morrison",
    ]
    for name in should_be_unstarred:
        contact = contact_map.get(name)
        if contact is None:
            errors.append(f"Contact '{name}' not found")
        elif contact.get("isStarred"):
            errors.append(f"'{name}' should be unstarred but is still starred")

    if errors:
        return False, "; ".join(errors)
    return True, "All starred contacts unstarred except Family members."
