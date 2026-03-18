import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find Engineering Team and Work groups by name
    contact_groups = state.get("contactGroups", [])
    eng_group = None
    work_group = None
    for g in contact_groups:
        if g.get("name") == "Engineering Team":
            eng_group = g
        elif g.get("name") == "Work":
            work_group = g

    if eng_group is None:
        return False, "Engineering Team group not found in contactGroups."
    if work_group is None:
        return False, "Work group not found in contactGroups."

    eng_id = eng_group["id"]
    work_id = work_group["id"]

    # Find all contacts in the Engineering Team group
    contacts = state.get("contacts", [])
    eng_contacts = [
        c for c in contacts if eng_id in c.get("groups", [])
    ]

    if len(eng_contacts) == 0:
        return False, "No contacts found in the Engineering Team group."

    # Verify all Engineering Team contacts are also in Work
    missing_work = []
    for c in eng_contacts:
        if work_id not in c.get("groups", []):
            name = f"{c.get('firstName', '')} {c.get('lastName', '')}".strip()
            missing_work.append(name)

    if missing_work:
        return False, (
            f"The following Engineering Team contacts are not in the Work group: "
            f"{', '.join(missing_work)}."
        )

    member_names = [
        f"{c.get('firstName', '')} {c.get('lastName', '')}".strip()
        for c in eng_contacts
    ]
    return True, (
        f"All {len(eng_contacts)} Engineering Team contacts are also in the Work group: "
        f"{', '.join(member_names)}."
    )
