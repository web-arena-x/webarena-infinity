import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])

    # Find Priya Sharma
    priya = None
    for c in contacts:
        if c.get("firstName") == "Priya" and c.get("lastName") == "Sharma":
            priya = c
            break

    if not priya:
        return False, "Contact with firstName='Priya' and lastName='Sharma' not found."

    # Verify job title
    if priya.get("jobTitle") != "VP of Engineering":
        return False, f"Expected jobTitle 'VP of Engineering', got '{priya.get('jobTitle')}'."

    # Find VIP group
    contact_groups = state.get("contactGroups", [])
    vip_group = None
    for g in contact_groups:
        if g.get("name") == "VIP":
            vip_group = g
            break

    if not vip_group:
        return False, "Contact group 'VIP' not found in contactGroups."

    vip_group_id = vip_group.get("id")
    priya_groups = priya.get("groups", [])

    if vip_group_id not in priya_groups:
        return False, f"VIP group ID '{vip_group_id}' not found in Priya Sharma's groups: {priya_groups}."

    return True, "Priya Sharma's job title updated to 'VP of Engineering' and added to VIP label."
