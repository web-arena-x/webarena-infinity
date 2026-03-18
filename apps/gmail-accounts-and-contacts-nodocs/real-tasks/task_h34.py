import requests
import re


def verify(server_url: str) -> tuple[bool, str]:
    """Verify Finance Network label with Investors + CFO/Finance/Banking contacts."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])
    contact_groups = state.get("contactGroups", [])

    # Find Finance Network label
    finance_group = None
    for g in contact_groups:
        if g.get("name") == "Finance Network":
            finance_group = g
            break

    if finance_group is None:
        return False, "Label 'Finance Network' not found."

    finance_id = finance_group["id"]

    # Find Investors label
    investors = None
    for g in contact_groups:
        if g.get("name") == "Investors":
            investors = g
            break

    if investors is None:
        return False, "Investors label not found."

    investors_id = investors["id"]

    # All Investors should be in Finance Network
    investor_contacts = [
        c for c in contacts if investors_id in c.get("groups", [])
    ]

    missing_investors = []
    for c in investor_contacts:
        name = f"{c.get('firstName', '')} {c.get('lastName', '')}".strip()
        if finance_id not in c.get("groups", []):
            missing_investors.append(name)

    if missing_investors:
        return False, (
            f"Investor contacts missing from Finance Network: "
            f"{', '.join(missing_investors)}."
        )

    # Contacts with CFO/Finance/Banking in title should also be in Finance Network
    title_pattern = re.compile(r"\b(CFO|Finance|Banking)\b", re.IGNORECASE)

    expected_title_matches = [
        ("Diana", "Ross-Taylor"),       # CFO
        ("Gabriella", "Romano"),         # Head of Digital Banking
        ("Rosa", "Gonzalez"),            # Open Banking Director
    ]

    missing_title = []
    for first, last in expected_title_matches:
        for c in contacts:
            if c.get("firstName") == first and c.get("lastName") == last:
                if finance_id not in c.get("groups", []):
                    missing_title.append(f"{first} {last}")
                break

    if missing_title:
        return False, (
            f"Contacts with CFO/Finance/Banking titles missing from "
            f"Finance Network: {', '.join(missing_title)}."
        )

    # Count total members — should be 9 (6 investors + 3 title matches)
    total_members = sum(
        1 for c in contacts if finance_id in c.get("groups", [])
    )
    if total_members < 9:
        return False, (
            f"Finance Network should have at least 9 members "
            f"(6 investors + 3 title matches), found {total_members}."
        )

    return True, (
        f"Finance Network label created with {total_members} members: "
        f"all Investors plus contacts with CFO/Finance/Banking titles."
    )
