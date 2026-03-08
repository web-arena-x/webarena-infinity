# Task: Star all Friends-labeled contacts who don't have Work label.
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

    # Friends (clabel_2) contacts without Work (clabel_3) should be starred
    should_be_starred = [
        "Ana Gutierrez",
        "Rachel Foster",
        "Chris Evans",
        "Samantha Lee",
        "Jake Morrison",
    ]

    for name in should_be_starred:
        contact = contact_map.get(name)
        if contact is None:
            errors.append(f"Contact '{name}' not found")
            continue
        if not contact.get("isStarred"):
            errors.append(f"'{name}' (Friends, no Work) should be starred but is not")

    if errors:
        return False, "; ".join(errors)
    return True, "All Friends-labeled contacts without Work label are now starred."
