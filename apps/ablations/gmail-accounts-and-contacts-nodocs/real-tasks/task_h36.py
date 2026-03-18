import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify HR Business Partner promoted: title updated, VIP, starred."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])
    contact_groups = state.get("contactGroups", [])

    # Find Megan Foster-Kim
    megan = None
    for c in contacts:
        if c.get("firstName") == "Megan" and c.get("lastName") == "Foster-Kim":
            megan = c
            break

    if megan is None:
        return False, "Megan Foster-Kim not found in contacts."

    # Check job title updated
    if megan.get("jobTitle") != "Head of People Operations":
        return False, (
            f"Job title should be 'Head of People Operations', "
            f"got {megan.get('jobTitle')!r}."
        )

    # Check starred
    if not megan.get("starred"):
        return False, "Megan Foster-Kim should be starred."

    # Check in VIP label
    vip = None
    for g in contact_groups:
        if g.get("name") == "VIP":
            vip = g
            break

    if vip is None:
        return False, "VIP label not found."

    if vip["id"] not in megan.get("groups", []):
        return False, "Megan Foster-Kim should be in the VIP label."

    return True, (
        "Megan Foster-Kim updated: title changed to Head of People Operations, "
        "starred, and added to VIP."
    )
