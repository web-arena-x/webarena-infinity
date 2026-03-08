# Task: Create contact Jordan Wells with email jordan.wells@wellsfargo.com and company Wells Fargo.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()
    errors = []

    contacts = state.get("contacts", [])
    match = [
        c for c in contacts
        if c.get("firstName") == "Jordan"
        and c.get("lastName") == "Wells"
        and c.get("email") == "jordan.wells@wellsfargo.com"
        and c.get("company") == "Wells Fargo"
    ]

    if not match:
        errors.append(
            "No contact found with firstName='Jordan', lastName='Wells', "
            "email='jordan.wells@wellsfargo.com', company='Wells Fargo'"
        )

    if errors:
        return False, "; ".join(errors)
    return True, "Contact Jordan Wells created with correct email and company."
