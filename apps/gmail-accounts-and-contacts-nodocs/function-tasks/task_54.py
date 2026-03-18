import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Check that "Investors" group no longer exists
    contact_groups = state.get("contactGroups", [])
    for g in contact_groups:
        if g.get("name") == "Investors":
            return False, "Contact group 'Investors' still exists. It should have been deleted."

    contacts = state.get("contacts", [])

    # Check Derek Hoffman still exists but grp_5 removed from groups
    derek = None
    for c in contacts:
        if c.get("firstName") == "Derek" and c.get("lastName") == "Hoffman":
            derek = c
            break

    if derek is None:
        return False, "Contact 'Derek Hoffman' not found. He should still exist after deleting the Investors label."

    if "grp_5" in derek.get("groups", []):
        return False, "Contact 'Derek Hoffman' still has 'grp_5' in groups. It should have been removed when the Investors label was deleted."

    # Verify Derek still has his other groups
    derek_groups = derek.get("groups", [])
    if "grp_6" not in derek_groups:
        return False, f"Contact 'Derek Hoffman' is missing 'grp_6' from groups. Current groups: {derek_groups}"
    if "grp_10" not in derek_groups:
        return False, f"Contact 'Derek Hoffman' is missing 'grp_10' from groups. Current groups: {derek_groups}"

    # Check Victoria Blackwell still exists but grp_5 removed from groups
    victoria = None
    for c in contacts:
        if c.get("firstName") == "Victoria" and c.get("lastName") == "Blackwell":
            victoria = c
            break

    if victoria is None:
        return False, "Contact 'Victoria Blackwell' not found. She should still exist after deleting the Investors label."

    if "grp_5" in victoria.get("groups", []):
        return False, "Contact 'Victoria Blackwell' still has 'grp_5' in groups. It should have been removed when the Investors label was deleted."

    return True, "Contact group 'Investors' deleted. Derek Hoffman and Victoria Blackwell no longer have 'grp_5' in their groups."
