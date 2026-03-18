import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify Stockholm Backend Engineer from directory added as contact in Work + Engineering Team."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])
    contact_groups = state.get("contactGroups", [])

    # Find Eric Johansson in contacts by email
    eric = None
    for c in contacts:
        if c.get("email") == "eric.johansson@techcorp.io":
            eric = c
            break

    if eric is None:
        return False, "Contact for eric.johansson@techcorp.io not found in contacts."

    # Verify name
    first = eric.get("firstName", "")
    last = eric.get("lastName", "")
    if "Eric" not in first or "Johansson" not in last:
        return False, f"Name mismatch: expected Eric Johansson, got {first} {last}."

    # Verify company
    if eric.get("company") != "TechCorp":
        return False, f"Company should be 'TechCorp', got {eric.get('company')!r}."

    # Verify job title present
    if not eric.get("jobTitle"):
        return False, "Job title is missing from the contact."

    # Find Work and Engineering Team labels
    work = None
    eng = None
    for g in contact_groups:
        if g.get("name") == "Work":
            work = g
        elif g.get("name") == "Engineering Team":
            eng = g

    if work is None:
        return False, "Work label not found."
    if eng is None:
        return False, "Engineering Team label not found."

    groups = eric.get("groups", [])
    if work["id"] not in groups:
        return False, "Eric Johansson is not in the Work label."
    if eng["id"] not in groups:
        return False, "Eric Johansson is not in the Engineering Team label."

    return True, (
        "Eric Johansson from Stockholm office added as contact with directory info, "
        "assigned to Work and Engineering Team labels."
    )
