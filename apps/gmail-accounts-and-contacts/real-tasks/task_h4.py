# Task: All Family contacts have Emergency and Friends labels.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()
    errors = []

    contacts = state.get("contacts", [])

    # Family contacts to check
    family_members = {
        "Margaret Johnson": None,
        "Richard Johnson": None,
        "Laura Johnson-Martinez": None,
        "Leo Martinez": None,
    }

    for c in contacts:
        full_name = f"{c.get('firstName', '')} {c.get('lastName', '')}".strip()
        if full_name in family_members:
            family_members[full_name] = c

    required_labels = {
        "clabel_1": "Family",
        "clabel_2": "Friends",
        "clabel_10": "Emergency",
    }

    for name, contact in family_members.items():
        if contact is None:
            errors.append(f"Family contact '{name}' not found")
            continue
        contact_labels = contact.get("labels", [])
        for label_id, label_name in required_labels.items():
            if label_id not in contact_labels:
                errors.append(f"'{name}' missing '{label_name}' label ({label_id})")

    if errors:
        return False, "; ".join(errors)
    return True, "All Family contacts have Family, Emergency, and Friends labels."
