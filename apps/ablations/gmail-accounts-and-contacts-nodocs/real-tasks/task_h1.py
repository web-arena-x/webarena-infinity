import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find the Investors group by name
    contact_groups = state.get("contactGroups", [])
    investors_group = None
    for g in contact_groups:
        if g.get("name") == "Investors":
            investors_group = g
            break

    if investors_group is None:
        return False, "Investors group not found in contactGroups."

    investors_id = investors_group["id"]

    # Find all contacts that belong to the Investors group
    contacts = state.get("contacts", [])
    investors_contacts = [
        c for c in contacts if investors_id in c.get("groups", [])
    ]

    if len(investors_contacts) == 0:
        return False, "No contacts found in the Investors group."

    # Verify ALL Investors contacts are starred
    unstarred = []
    for c in investors_contacts:
        if not c.get("starred", False):
            name = f"{c.get('firstName', '')} {c.get('lastName', '')}".strip()
            unstarred.append(name)

    if unstarred:
        return False, f"The following Investors contacts are not starred: {', '.join(unstarred)}."

    # Verify we have at least 6 members (the expected count)
    if len(investors_contacts) < 6:
        return False, (
            f"Expected at least 6 contacts in Investors group, found {len(investors_contacts)}."
        )

    return True, (
        f"All {len(investors_contacts)} contacts in the Investors group are starred."
    )
