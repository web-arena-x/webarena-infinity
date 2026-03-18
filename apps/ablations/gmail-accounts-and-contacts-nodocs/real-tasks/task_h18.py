import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contact_groups = state.get("contactGroups", [])
    contacts = state.get("contacts", [])

    # Find the Swedish Contacts group
    swedish_group = None
    for g in contact_groups:
        if g.get("name") == "Swedish Contacts":
            swedish_group = g
            break

    if swedish_group is None:
        return False, "Group 'Swedish Contacts' not found in contactGroups."

    swedish_id = swedish_group["id"]

    # Expected contacts with +46 phone numbers
    expected_swedish = [
        ("Sophia", "Andersson"),
        ("Nora", "Eriksson"),
        ("Ingrid", "Johansson"),
        ("Oscar", "Lindqvist"),
        ("Julia", "Svensson"),
        ("Peter", "Strand"),
        ("Anders", "Bjornsson"),
    ]

    # Verify all 7 have the Swedish Contacts group
    missing = []
    for first, last in expected_swedish:
        found = False
        for c in contacts:
            if c.get("firstName") == first and c.get("lastName") == last:
                found = True
                if swedish_id not in c.get("groups", []):
                    missing.append(f"{first} {last}")
                break
        if not found:
            missing.append(f"{first} {last} (not found)")

    if missing:
        return False, (
            f"The following +46 contacts are missing the Swedish Contacts label: "
            f"{', '.join(missing)}."
        )

    # Verify no OTHER contacts have this group
    swedish_names = {f"{f} {l}" for f, l in expected_swedish}
    extra = []
    for c in contacts:
        name = f"{c.get('firstName', '')} {c.get('lastName', '')}".strip()
        if swedish_id in c.get("groups", []) and name not in swedish_names:
            extra.append(name)

    if extra:
        return False, (
            f"The following contacts have the Swedish Contacts label but should not: "
            f"{', '.join(extra)}."
        )

    return True, (
        "Swedish Contacts group created with all 7 contacts who have +46 phone "
        "numbers. No other contacts have this label."
    )
