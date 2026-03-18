import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contact_groups = state.get("contactGroups", [])
    contacts = state.get("contacts", [])

    # Find the VIP group by name
    vip_group = None
    for g in contact_groups:
        if g.get("name") == "VIP":
            vip_group = g
            break

    if vip_group is None:
        return False, "VIP group not found in contactGroups."

    vip_id = vip_group["id"]

    # Helper to find a contact by name
    def find_contact(first, last):
        for c in contacts:
            if c.get("firstName") == first and c.get("lastName") == last:
                return c
        return None

    # TechCorp members who should REMAIN in VIP
    should_have_vip = [
        ("Marcus", "Johnson"),
        ("Diana", "Ross-Taylor"),
        ("Priya", "Sharma"),
        ("James", "Wu"),
    ]

    for first, last in should_have_vip:
        c = find_contact(first, last)
        if c is None:
            return False, f"Contact '{first} {last}' not found."
        if vip_id not in c.get("groups", []):
            return False, (
                f"{first} {last} should be in the VIP group but is not."
            )

    # Non-TechCorp contacts who should have been REMOVED from VIP
    should_not_have_vip = [
        ("Derek", "Hoffman"),
        ("Victoria", "Blackwell"),
        ("Catherine", "Duval"),
        ("Satoshi", "Yamamoto"),
        ("Douglas", "Kim"),
        ("Jessica", "Singh"),
        ("Ethan", "Goldstein"),
        ("Nicholas", "Harper"),
    ]

    for first, last in should_not_have_vip:
        c = find_contact(first, last)
        if c is None:
            continue  # Contact might still exist but without VIP
        if vip_id in c.get("groups", []):
            return False, (
                f"{first} {last} should have been removed from VIP "
                f"(not a TechCorp employee) but still has the VIP label."
            )

    # Count total contacts with VIP — should be exactly 4
    vip_contacts = [c for c in contacts if vip_id in c.get("groups", [])]
    if len(vip_contacts) != 4:
        vip_names = [
            f"{c.get('firstName', '')} {c.get('lastName', '')}".strip()
            for c in vip_contacts
        ]
        return False, (
            f"Expected exactly 4 contacts in VIP, found {len(vip_contacts)}: "
            f"{', '.join(vip_names)}."
        )

    return True, (
        "VIP group updated correctly: Marcus Johnson, Diana Ross-Taylor, "
        "Priya Sharma, and James Wu are the only 4 members. "
        "All non-TechCorp contacts removed."
    )
