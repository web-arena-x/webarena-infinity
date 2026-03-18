import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find Patricia Nguyen
    contacts = state.get("contacts", [])
    patricia = None
    for c in contacts:
        if c.get("firstName") == "Patricia" and c.get("lastName") == "Nguyen":
            patricia = c
            break

    if patricia is None:
        return False, "Contact Patricia Nguyen not found."

    errors = []

    # Verify email
    if patricia.get("email") != "patricia.nguyen@techcorp.io":
        errors.append(
            f"Email is '{patricia.get('email')}', "
            f"expected 'patricia.nguyen@techcorp.io'."
        )

    # Verify phone
    if patricia.get("phone") != "+1 (415) 555-4000":
        errors.append(
            f"Phone is '{patricia.get('phone')}', "
            f"expected '+1 (415) 555-4000'."
        )

    # Verify company
    if patricia.get("company") != "TechCorp":
        errors.append(
            f"Company is '{patricia.get('company')}', expected 'TechCorp'."
        )

    # Verify job title
    if patricia.get("jobTitle") != "Chief of Staff":
        errors.append(
            f"Job title is '{patricia.get('jobTitle')}', expected 'Chief of Staff'."
        )

    # Verify starred
    if not patricia.get("starred", False):
        errors.append("Contact is not starred.")

    # Find Work and VIP groups by name
    contact_groups = state.get("contactGroups", [])
    work_group = None
    vip_group = None
    for g in contact_groups:
        if g.get("name") == "Work":
            work_group = g
        elif g.get("name") == "VIP":
            vip_group = g

    if work_group is None:
        errors.append("Work group not found in contactGroups.")
    else:
        if work_group["id"] not in patricia.get("groups", []):
            errors.append(
                f"Patricia Nguyen is not in the Work group "
                f"(groups: {patricia.get('groups', [])})."
            )

    if vip_group is None:
        errors.append("VIP group not found in contactGroups.")
    else:
        if vip_group["id"] not in patricia.get("groups", []):
            errors.append(
                f"Patricia Nguyen is not in the VIP group "
                f"(groups: {patricia.get('groups', [])})."
            )

    if errors:
        return False, " ".join(errors)

    return True, (
        "Patricia Nguyen contact created correctly with email "
        "patricia.nguyen@techcorp.io, phone +1 (415) 555-4000, company TechCorp, "
        "job title Chief of Staff, starred, and in both Work and VIP groups."
    )
