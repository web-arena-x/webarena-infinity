import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify CFO contact updated with notes, starred, and added to Family."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])
    contact_groups = state.get("contactGroups", [])

    # Find Diana Ross-Taylor (CFO)
    diana = None
    for c in contacts:
        if c.get("firstName") == "Diana" and c.get("lastName") == "Ross-Taylor":
            diana = c
            break

    if diana is None:
        return False, "Diana Ross-Taylor not found in contacts."

    # Verify notes
    notes = diana.get("notes", "")
    if "Executive sponsor for Q2 initiative" not in notes:
        return False, (
            f"Notes should contain 'Executive sponsor for Q2 initiative', "
            f"got {notes!r}."
        )

    # Verify starred
    if not diana.get("starred"):
        return False, "Diana Ross-Taylor should be starred."

    # Verify in Family label
    family = None
    for g in contact_groups:
        if g.get("name") == "Family":
            family = g
            break

    if family is None:
        return False, "Family label not found."

    if family["id"] not in diana.get("groups", []):
        return False, "Diana Ross-Taylor should be in the Family label."

    return True, (
        "Diana Ross-Taylor (CFO) updated: notes added, starred, "
        "and added to Family label."
    )
