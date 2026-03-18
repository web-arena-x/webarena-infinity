import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contact_groups = state.get("contactGroups", [])
    contacts = state.get("contacts", [])

    # Find Advisors group
    advisors_group = None
    for g in contact_groups:
        if g.get("name") == "Advisors":
            advisors_group = g
            break

    if advisors_group is None:
        return False, "Group 'Advisors' not found in contactGroups."

    advisors_id = advisors_group["id"]

    # Find Board group
    board_group = None
    for g in contact_groups:
        if g.get("name") == "Board":
            board_group = g
            break

    if board_group is None:
        return False, "Group 'Board' not found in contactGroups."

    board_id = board_group["id"]

    # Verify Investors group still exists
    investors_exists = False
    for g in contact_groups:
        if g.get("name") == "Investors":
            investors_exists = True
            break

    if not investors_exists:
        return False, (
            "Investors group no longer exists. The task did not ask to delete it."
        )

    # Investors members: Derek Hoffman, Victoria Blackwell, Hiroshi Tanaka,
    # Catherine Duval, Ibrahim Okafor, Ethan Goldstein
    investors_members = [
        ("Derek", "Hoffman"),
        ("Victoria", "Blackwell"),
        ("Hiroshi", "Tanaka"),
        ("Catherine", "Duval"),
        ("Ibrahim", "Okafor"),
        ("Ethan", "Goldstein"),
    ]

    # All Investors members should have the Advisors group
    missing_advisors = []
    for first, last in investors_members:
        for c in contacts:
            if c.get("firstName") == first and c.get("lastName") == last:
                if advisors_id not in c.get("groups", []):
                    missing_advisors.append(f"{first} {last}")
                break
        else:
            missing_advisors.append(f"{first} {last} (not found)")

    if missing_advisors:
        return False, (
            f"The following Investors contacts are missing the Advisors label: "
            f"{', '.join(missing_advisors)}."
        )

    # Derek Hoffman and Victoria Blackwell should also have the Board group
    board_members = [
        ("Derek", "Hoffman"),
        ("Victoria", "Blackwell"),
    ]

    missing_board = []
    for first, last in board_members:
        for c in contacts:
            if c.get("firstName") == first and c.get("lastName") == last:
                if board_id not in c.get("groups", []):
                    missing_board.append(f"{first} {last}")
                break

    if missing_board:
        return False, (
            f"The following contacts are missing the Board label: "
            f"{', '.join(missing_board)}."
        )

    return True, (
        "Advisors and Board groups created. All 6 Investors contacts have the "
        "Advisors label. Derek Hoffman and Victoria Blackwell also have the "
        "Board label. Investors group still exists."
    )
