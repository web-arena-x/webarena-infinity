import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find Book Club and Friends groups by name
    contact_groups = state.get("contactGroups", [])
    book_club_group = None
    friends_group = None
    for g in contact_groups:
        if g.get("name") == "Book Club":
            book_club_group = g
        elif g.get("name") == "Friends":
            friends_group = g

    if book_club_group is None:
        return False, "Book Club group not found in contactGroups."
    if friends_group is None:
        return False, "Friends group not found in contactGroups."

    book_club_id = book_club_group["id"]
    friends_id = friends_group["id"]

    # Find all contacts in Book Club
    contacts = state.get("contacts", [])
    book_club_contacts = [
        c for c in contacts if book_club_id in c.get("groups", [])
    ]

    if len(book_club_contacts) == 0:
        return False, "No contacts found in the Book Club group."

    # Verify all Book Club contacts are also in Friends
    missing_friends = []
    for c in book_club_contacts:
        if friends_id not in c.get("groups", []):
            name = f"{c.get('firstName', '')} {c.get('lastName', '')}".strip()
            missing_friends.append(name)

    if missing_friends:
        return False, (
            f"The following Book Club contacts are not in the Friends group: "
            f"{', '.join(missing_friends)}."
        )

    member_names = [
        f"{c.get('firstName', '')} {c.get('lastName', '')}".strip()
        for c in book_club_contacts
    ]
    return True, (
        f"All {len(book_club_contacts)} Book Club contacts are also in Friends: "
        f"{', '.join(member_names)}."
    )
