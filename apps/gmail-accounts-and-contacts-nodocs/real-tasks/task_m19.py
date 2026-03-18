import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find Hannah Cohen
    contacts = state.get("contacts", [])
    hannah = None
    for c in contacts:
        if c.get("firstName") == "Hannah" and c.get("lastName") == "Cohen":
            hannah = c
            break

    if hannah is None:
        return False, "Contact Hannah Cohen not found in contacts list."

    errors = []

    # Check email updated
    if hannah.get("email") != "hannah.cohen@gmail.com":
        errors.append(
            f"Expected email='hannah.cohen@gmail.com', got '{hannah.get('email')}'."
        )

    # Find Work group ID
    contact_groups = state.get("contactGroups", [])
    work_group_id = None
    for g in contact_groups:
        if g.get("name") == "Work":
            work_group_id = g.get("id")
            break

    if work_group_id is None:
        errors.append("Contact group 'Work' not found, cannot verify group removal.")
    else:
        if work_group_id in hannah.get("groups", []):
            errors.append(
                f"Hannah Cohen still has Work group ('{work_group_id}') in her groups: {hannah.get('groups', [])}."
            )

    if errors:
        return False, " ".join(errors)

    return True, "Hannah Cohen's email updated to hannah.cohen@gmail.com and removed from Work label."
