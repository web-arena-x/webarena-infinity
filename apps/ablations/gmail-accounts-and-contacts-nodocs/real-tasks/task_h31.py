import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify Key Contacts label with all starred contacts that have 2+ labels."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])
    contact_groups = state.get("contactGroups", [])

    # Find Key Contacts label
    key_group = None
    for g in contact_groups:
        if g.get("name") == "Key Contacts":
            key_group = g
            break

    if key_group is None:
        return False, "Label 'Key Contacts' not found."

    key_id = key_group["id"]

    # Expected: starred contacts with 2+ labels (excluding Key Contacts itself)
    expected = [
        ("James", "Wu"),
        ("Priya", "Sharma"),
        ("Marcus", "Johnson"),
        ("Jake", "Morrison"),
        ("Ben", "Watkins"),
        ("Derek", "Hoffman"),
        ("Victoria", "Blackwell"),
        ("Satoshi", "Yamamoto"),
        ("Jessica", "Singh"),
        ("Ethan", "Goldstein"),
    ]

    # Verify all expected contacts are in Key Contacts
    missing = []
    for first, last in expected:
        for c in contacts:
            if c.get("firstName") == first and c.get("lastName") == last:
                if key_id not in c.get("groups", []):
                    missing.append(f"{first} {last}")
                break

    if missing:
        return False, (
            f"These starred contacts with 2+ labels are missing from "
            f"Key Contacts: {', '.join(missing)}."
        )

    # Verify no contacts that shouldn't be there
    expected_names = {f"{f} {l}" for f, l in expected}
    extra = []
    for c in contacts:
        name = f"{c.get('firstName', '')} {c.get('lastName', '')}".strip()
        if key_id in c.get("groups", []) and name not in expected_names:
            extra.append(name)

    if extra:
        return False, (
            f"These contacts should not be in Key Contacts "
            f"(not starred or have fewer than 2 labels): "
            f"{', '.join(extra)}."
        )

    return True, (
        f"Key Contacts label created with all {len(expected)} starred contacts "
        f"that belong to 2+ labels."
    )
