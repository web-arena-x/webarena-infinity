import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    contact_groups = state.get("contactGroups", [])
    group_names = [g.get("name") for g in contact_groups]

    errors = []

    # Old names should no longer exist
    if "Vendors" in group_names:
        errors.append("Group 'Vendors' still exists (should have been renamed to 'Technology Partners').")

    if "Conference Contacts" in group_names:
        errors.append("Group 'Conference Contacts' still exists (should have been renamed to 'Industry Network').")

    # New names should exist
    if "Technology Partners" not in group_names:
        errors.append("Group 'Technology Partners' not found (expected rename from 'Vendors').")

    if "Industry Network" not in group_names:
        errors.append("Group 'Industry Network' not found (expected rename from 'Conference Contacts').")

    if errors:
        return False, " ".join(errors)

    return True, "Labels renamed: 'Vendors' -> 'Technology Partners' and 'Conference Contacts' -> 'Industry Network'."
