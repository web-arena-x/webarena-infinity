import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find the Conference Contacts group by name
    contact_groups = state.get("contactGroups", [])
    conf_group = None
    for g in contact_groups:
        if g.get("name") == "Conference Contacts":
            conf_group = g
            break

    if conf_group is None:
        return False, "Conference Contacts group not found. It should still exist."

    conf_id = conf_group["id"]

    # Check that no TechCorp contact has the Conference Contacts group
    contacts = state.get("contacts", [])
    techcorp_in_conf = []
    for c in contacts:
        company = (c.get("company") or "").lower()
        if company == "techcorp" and conf_id in c.get("groups", []):
            name = f"{c.get('firstName', '')} {c.get('lastName', '')}".strip()
            techcorp_in_conf.append(name)

    if techcorp_in_conf:
        return False, (
            f"The following TechCorp contacts are still in Conference Contacts: "
            f"{', '.join(techcorp_in_conf)}."
        )

    # Verify that Conference Contacts still has non-TechCorp members
    non_techcorp_in_conf = []
    for c in contacts:
        company = (c.get("company") or "").lower()
        if company != "techcorp" and conf_id in c.get("groups", []):
            name = f"{c.get('firstName', '')} {c.get('lastName', '')}".strip()
            non_techcorp_in_conf.append(name)

    if len(non_techcorp_in_conf) == 0:
        return False, (
            "Conference Contacts group has no remaining members. "
            "Non-TechCorp contacts should still be in the group."
        )

    return True, (
        f"No TechCorp contacts are in Conference Contacts. "
        f"{len(non_techcorp_in_conf)} non-TechCorp contacts remain in the group."
    )
