import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify all contacts with Japanese phone numbers removed from Conference Contacts."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])
    contact_groups = state.get("contactGroups", [])

    # Find Conference Contacts label
    conf = None
    for g in contact_groups:
        if g.get("name") == "Conference Contacts":
            conf = g
            break

    if conf is None:
        return False, "Conference Contacts label not found."

    conf_id = conf["id"]

    # Expected Japanese contacts to be removed from Conference Contacts
    expected_removed = [
        ("Satoshi", "Yamamoto"),
        ("Yuki", "Nakamura"),
        ("Naomi", "Ito"),
        ("Takeshi", "Mori"),
    ]

    # Verify they are no longer in Conference Contacts
    still_in = []
    for first, last in expected_removed:
        for c in contacts:
            if c.get("firstName") == first and c.get("lastName") == last:
                if conf_id in c.get("groups", []):
                    still_in.append(f"{first} {last}")
                break

    if still_in:
        return False, (
            f"Japanese contacts still in Conference Contacts: "
            f"{', '.join(still_in)}."
        )

    # Verify contacts still exist (should not be deleted, only removed from label)
    missing = []
    for first, last in expected_removed:
        found = False
        for c in contacts:
            if c.get("firstName") == first and c.get("lastName") == last:
                found = True
                break
        if not found:
            missing.append(f"{first} {last}")

    if missing:
        return False, (
            f"Contacts should still exist (only removed from label, not deleted): "
            f"{', '.join(missing)}."
        )

    # Verify non-Japanese conference contacts are untouched
    remaining_conf = [
        c for c in contacts if conf_id in c.get("groups", [])
    ]
    if len(remaining_conf) < 30:
        return False, (
            f"Too many contacts removed from Conference Contacts. "
            f"Only 4 Japanese contacts should have been removed. "
            f"Found {len(remaining_conf)} remaining, expected ~35."
        )

    return True, (
        "All 4 Japanese phone number (+81) contacts removed from "
        "Conference Contacts label. Contacts still exist."
    )
