import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify Sequoia Capital contact transitioned to independent advisor."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])
    contact_groups = state.get("contactGroups", [])

    # Find Victoria Blackwell
    victoria = None
    for c in contacts:
        if c.get("firstName") == "Victoria" and c.get("lastName") == "Blackwell":
            victoria = c
            break

    if victoria is None:
        return False, "Victoria Blackwell not found in contacts."

    # Check company updated
    if victoria.get("company") != "Independent Advisor":
        return False, (
            f"Company should be 'Independent Advisor', "
            f"got {victoria.get('company')!r}."
        )

    # Check unstarred
    if victoria.get("starred"):
        return False, "Victoria Blackwell should be unstarred."

    # Check NOT in Investors
    investors = None
    for g in contact_groups:
        if g.get("name") == "Investors":
            investors = g
            break

    if investors and investors["id"] in victoria.get("groups", []):
        return False, "Victoria Blackwell should not be in the Investors label."

    # Check Former Investors label exists and Victoria is in it
    former = None
    for g in contact_groups:
        if g.get("name") == "Former Investors":
            former = g
            break

    if former is None:
        return False, "Label 'Former Investors' not found."

    if former["id"] not in victoria.get("groups", []):
        return False, "Victoria Blackwell should be in the 'Former Investors' label."

    return True, (
        "Victoria Blackwell updated: company changed to Independent Advisor, "
        "unstarred, moved from Investors to Former Investors."
    )
