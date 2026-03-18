import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contact_groups = state.get("contactGroups", [])
    contacts = state.get("contacts", [])

    # Verify College Alumni group no longer exists
    for g in contact_groups:
        if g.get("name") == "College Alumni":
            return False, "The 'College Alumni' group still exists. It should have been deleted."

    # Also verify no contact references the old group ID (grp_6)
    contacts_with_grp6 = []
    for c in contacts:
        if "grp_6" in c.get("groups", []):
            name = f"{c.get('firstName', '')} {c.get('lastName', '')}".strip()
            contacts_with_grp6.append(name)

    if contacts_with_grp6:
        return False, (
            f"The following contacts still reference the College Alumni group ID 'grp_6': "
            f"{', '.join(contacts_with_grp6)}."
        )

    # Jake Morrison was starred and was ONLY in College Alumni + Friends (not VIP/Investors)
    # He should now be unstarred
    jake = None
    for c in contacts:
        if c.get("firstName") == "Jake" and c.get("lastName") == "Morrison":
            jake = c
            break

    if jake is None:
        return False, "Contact 'Jake Morrison' not found."

    if jake.get("starred") is True:
        return False, (
            "Jake Morrison should be unstarred because he was in College Alumni "
            "but not in VIP or Investors."
        )

    # Derek Hoffman was starred and is in Investors (grp_5) and VIP (grp_10)
    # He should remain starred
    derek = None
    for c in contacts:
        if c.get("firstName") == "Derek" and c.get("lastName") == "Hoffman":
            derek = c
            break

    if derek is None:
        return False, "Contact 'Derek Hoffman' not found."

    if derek.get("starred") is not True:
        return False, (
            "Derek Hoffman should remain starred because he is also in "
            "Investors and VIP groups."
        )

    return True, (
        "College Alumni group deleted, Jake Morrison unstarred, "
        "Derek Hoffman remains starred, and no contacts reference grp_6."
    )
