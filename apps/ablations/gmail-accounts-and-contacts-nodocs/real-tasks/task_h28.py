import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify non-Eng/Design directory employees not in contacts were added."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])
    contact_groups = state.get("contactGroups", [])

    # These directory employees are NOT in Engineering or Design departments
    # and were NOT in the original contacts — they should now exist
    expected_new = [
        {
            "email": "david.park@techcorp.io",
            "first": "David", "last": "Park",
            "title": "Senior Product Manager",
        },
        {
            "email": "jennifer.walsh@techcorp.io",
            "first": "Jennifer", "last": "Walsh",
            "title": "General Counsel",
        },
        {
            "email": "tony.russo@techcorp.io",
            "first": "Tony", "last": "Russo",
            "title": "Account Executive",
        },
        {
            "email": "elaine.cho@techcorp.io",
            "first": "Elaine", "last": "Cho",
            "title": "Marketing Director",
        },
        {
            "email": "maria.santos@techcorp.io",
            "first": "Maria", "last": "Santos",
            "title": "Support Team Lead",
        },
    ]

    # Find Work label
    work = None
    for g in contact_groups:
        if g.get("name") == "Work":
            work = g
            break

    if work is None:
        return False, "Work label not found."

    work_id = work["id"]

    missing = []
    not_in_work = []
    wrong_company = []

    for entry in expected_new:
        found = None
        for c in contacts:
            if c.get("email") == entry["email"]:
                found = c
                break

        if found is None:
            missing.append(f"{entry['first']} {entry['last']}")
            continue

        if found.get("company") != "TechCorp":
            wrong_company.append(
                f"{entry['first']} {entry['last']} "
                f"(got {found.get('company')!r})"
            )

        if work_id not in found.get("groups", []):
            not_in_work.append(f"{entry['first']} {entry['last']}")

    if missing:
        return False, (
            f"Missing contacts from directory: {', '.join(missing)}."
        )

    if wrong_company:
        return False, (
            f"Company should be 'TechCorp' for: {', '.join(wrong_company)}."
        )

    if not_in_work:
        return False, (
            f"Not in Work label: {', '.join(not_in_work)}."
        )

    return True, (
        f"All 5 non-Engineering/Design directory employees added as contacts "
        f"with TechCorp company and Work label."
    )
