import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find Kira Volkov
    contacts = state.get("contacts", [])
    kira = None
    for c in contacts:
        if c.get("firstName") == "Kira" and c.get("lastName") == "Volkov":
            kira = c
            break

    if kira is None:
        return False, "Contact Kira Volkov not found."

    errors = []

    # Check job title
    if kira.get("jobTitle") != "Junior Backend Engineer":
        errors.append(
            f"Job title is '{kira.get('jobTitle')}', expected 'Junior Backend Engineer'."
        )

    # Check starred
    if not kira.get("starred", False):
        errors.append("Contact is not starred.")

    # Find VIP group by name
    contact_groups = state.get("contactGroups", [])
    vip_group = None
    for g in contact_groups:
        if g.get("name") == "VIP":
            vip_group = g
            break

    if vip_group is None:
        errors.append("VIP group not found in contactGroups.")
    else:
        vip_id = vip_group["id"]
        if vip_id not in kira.get("groups", []):
            errors.append(
                f"Kira Volkov is not in the VIP group (groups: {kira.get('groups', [])})."
            )

    if errors:
        return False, " ".join(errors)

    return True, (
        "Kira Volkov's job title is 'Junior Backend Engineer', she is starred, "
        "and she is in the VIP group."
    )
