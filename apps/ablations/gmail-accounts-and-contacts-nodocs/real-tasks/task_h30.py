import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify two ByteDance Zhaos handled: Helen starred+VIP, Wei removed from Conference."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])
    contact_groups = state.get("contactGroups", [])

    # Find the two Zhao contacts at ByteDance
    helen = None
    wei = None
    for c in contacts:
        if c.get("lastName") == "Zhao":
            if c.get("firstName") == "Helen":
                helen = c
            elif c.get("firstName") == "Wei":
                wei = c

    if helen is None:
        return False, "Helen Zhao not found in contacts."
    if wei is None:
        return False, "Wei Zhao not found in contacts (should still exist)."

    # Find VIP and Conference Contacts labels
    vip = None
    conf = None
    for g in contact_groups:
        if g.get("name") == "VIP":
            vip = g
        elif g.get("name") == "Conference Contacts":
            conf = g

    if vip is None:
        return False, "VIP label not found."
    if conf is None:
        return False, "Conference Contacts label not found."

    # Helen (Data Privacy Counsel) should be starred and in VIP
    if not helen.get("starred"):
        return False, "Helen Zhao (data privacy) should be starred."
    if vip["id"] not in helen.get("groups", []):
        return False, "Helen Zhao (data privacy) should be in VIP label."

    # Wei (Director of Infrastructure) should NOT be in Conference Contacts
    if conf["id"] in wei.get("groups", []):
        return False, (
            "Wei Zhao (infrastructure) should be removed from "
            "Conference Contacts label."
        )

    return True, (
        "Helen Zhao (data privacy) starred and added to VIP. "
        "Wei Zhao (infrastructure) removed from Conference Contacts."
    )
