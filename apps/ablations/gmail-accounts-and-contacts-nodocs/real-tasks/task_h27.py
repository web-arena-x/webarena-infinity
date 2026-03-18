import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify all Family members unstarred except the youngest (Kevin Chen, 1995)."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])
    contact_groups = state.get("contactGroups", [])

    # Find Family group
    family = None
    for g in contact_groups:
        if g.get("name") == "Family":
            family = g
            break

    if family is None:
        return False, "Family label not found."

    family_id = family["id"]

    # Get all Family members
    family_contacts = [
        c for c in contacts if family_id in c.get("groups", [])
    ]

    if len(family_contacts) < 3:
        return False, (
            f"Expected at least 3 Family members, found {len(family_contacts)}."
        )

    # Kevin Chen (1995-03-15) is the youngest — should remain starred
    kevin = None
    incorrectly_starred = []
    for c in family_contacts:
        name = f"{c.get('firstName', '')} {c.get('lastName', '')}".strip()
        if c.get("firstName") == "Kevin" and c.get("lastName") == "Chen":
            kevin = c
        elif c.get("starred"):
            incorrectly_starred.append(name)

    if kevin is None:
        return False, "Kevin Chen not found in Family label."

    if not kevin.get("starred"):
        return False, (
            "Kevin Chen (youngest family member, born 1995-03-15) "
            "should still be starred."
        )

    if incorrectly_starred:
        return False, (
            f"These Family members should be unstarred (not the youngest): "
            f"{', '.join(incorrectly_starred)}."
        )

    return True, (
        "All Family members unstarred except Kevin Chen (youngest, born 1995). "
        f"{len(family_contacts)} family members verified."
    )
