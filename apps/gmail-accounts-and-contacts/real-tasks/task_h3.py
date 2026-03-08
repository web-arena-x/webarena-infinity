# Task: Delete all TechCorp contacts.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()
    errors = []

    contacts = state.get("contacts", [])

    # Check no contact with company='TechCorp'
    techcorp_contacts = [c for c in contacts if c.get("company") == "TechCorp"]
    if techcorp_contacts:
        names = [
            f"{c.get('firstName', '')} {c.get('lastName', '')}".strip()
            for c in techcorp_contacts
        ]
        errors.append(f"TechCorp contacts still exist: {', '.join(names)}")

    # Check total count decreased (seed had 40, should be 37 or fewer)
    if len(contacts) > 37:
        errors.append(
            f"Expected at most 37 contacts after deleting 3 TechCorp contacts, found {len(contacts)}"
        )

    if errors:
        return False, "; ".join(errors)
    return True, "All TechCorp contacts successfully deleted."
