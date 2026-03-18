import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])

    # Find Taylor Morgan
    taylor = None
    for c in contacts:
        if c.get("firstName") == "Taylor" and c.get("lastName") == "Morgan":
            taylor = c
            break

    if not taylor:
        return False, "Contact with firstName='Taylor' and lastName='Morgan' not found."

    # Verify email
    if taylor.get("email") != "taylor.morgan@techcorp.io":
        return False, f"Expected email 'taylor.morgan@techcorp.io', got '{taylor.get('email')}'."

    # Verify company
    if taylor.get("company") != "TechCorp":
        return False, f"Expected company 'TechCorp', got '{taylor.get('company')}'."

    # Verify job title
    if taylor.get("jobTitle") != "Marketing Manager":
        return False, f"Expected jobTitle 'Marketing Manager', got '{taylor.get('jobTitle')}'."

    # Verify phone
    if taylor.get("phone") != "+1 (415) 555-3500":
        return False, f"Expected phone '+1 (415) 555-3500', got '{taylor.get('phone')}'."

    # Find the Work group
    contact_groups = state.get("contactGroups", [])
    work_group = None
    for g in contact_groups:
        if g.get("name") == "Work":
            work_group = g
            break

    if not work_group:
        return False, "Contact group 'Work' not found in contactGroups."

    work_group_id = work_group.get("id")
    taylor_groups = taylor.get("groups", [])

    if work_group_id not in taylor_groups:
        return False, f"Work group ID '{work_group_id}' not found in Taylor Morgan's groups: {taylor_groups}."

    return True, "Taylor Morgan contact created correctly with all fields and Work label."
