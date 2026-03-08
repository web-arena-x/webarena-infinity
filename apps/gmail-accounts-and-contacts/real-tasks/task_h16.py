# Task: Unstar all, then star only James O'Brien and David Kim.
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

    # Should be starred
    should_be_starred = ["James O'Brien", "David Kim"]
    for name in should_be_starred:
        contact = contact_map.get(name)
        if contact is None:
            errors.append(f"Contact '{name}' not found")
        elif not contact.get("isStarred"):
            errors.append(f"'{name}' should be starred but is not")

    # Previously starred contacts should be unstarred
    should_be_unstarred = [
        "Sarah Chen",
        "Marcus Williams",
        "Emily Rodriguez",
        "Priya Sharma",
        "Kevin Zhao",
        "Maya Patel",
        "Margaret Johnson",
        "Richard Johnson",
        "Laura Johnson-Martinez",
        "Jake Morrison",
    ]
    for name in should_be_unstarred:
        contact = contact_map.get(name)
        if contact is None:
            # Contact might have been removed by other operations, skip
            continue
        if contact.get("isStarred"):
            errors.append(f"'{name}' should be unstarred but is still starred")

    if errors:
        return False, "; ".join(errors)
    return True, "All contacts unstarred; James O'Brien and David Kim starred."
