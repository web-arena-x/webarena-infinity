import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])

    # These contacts originally had empty groups arrays and should be removed
    ungrouped_contacts = [
        ("Natalie", "Dubois"),
        ("Henry", "Wright"),
        ("Leah", "Mitchell"),
        ("Jasmine", "Tran"),
        ("Rebecca", "Stone"),
        ("Timothy", "Buchanan"),
        ("Sophie", "Williams"),
        ("Penny", "Crawford"),
    ]

    # Check that none of the ungrouped contacts remain
    still_present = []
    for first, last in ungrouped_contacts:
        for c in contacts:
            if c.get("firstName") == first and c.get("lastName") == last:
                still_present.append(f"{first} {last}")
                break

    if still_present:
        return False, (
            f"The following ungrouped contacts were not removed: "
            f"{', '.join(still_present)}."
        )

    # Verify total contact count is 112 (120 - 8)
    if len(contacts) != 112:
        return False, (
            f"Expected 112 contacts after removing 8 ungrouped contacts, "
            f"but found {len(contacts)}."
        )

    return True, (
        "All 8 ungrouped contacts have been removed. "
        "Contact count is correctly 112."
    )
