import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify CEO-reporting contacts are in VIP and starred."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])
    contact_groups = state.get("contactGroups", [])

    # Find VIP label
    vip = None
    for g in contact_groups:
        if g.get("name") == "VIP":
            vip = g
            break

    if vip is None:
        return False, "VIP label not found."

    vip_id = vip["id"]

    # Directory employees who report to CEO AND are already in contacts:
    # Marcus Johnson (VP of Engineering) — already VIP + starred
    # Diana Ross-Taylor (CFO) — already VIP, not starred
    # Carlos Mendoza (Head of Sales) — not VIP, not starred
    # Sophia Andersson (Head of EU Operations) — not VIP, not starred
    # (Elaine Cho and Jennifer Walsh report to CEO but are NOT in contacts)

    ceo_reports = [
        ("Marcus", "Johnson"),
        ("Diana", "Ross-Taylor"),
        ("Carlos", "Mendoza"),
        ("Sophia", "Andersson"),
    ]

    not_vip = []
    not_starred = []

    for first, last in ceo_reports:
        for c in contacts:
            if c.get("firstName") == first and c.get("lastName") == last:
                name = f"{first} {last}"
                if vip_id not in c.get("groups", []):
                    not_vip.append(name)
                if not c.get("starred"):
                    not_starred.append(name)
                break

    if not_vip:
        return False, (
            f"CEO-reporting contacts not in VIP: {', '.join(not_vip)}."
        )

    if not_starred:
        return False, (
            f"CEO-reporting contacts not starred: {', '.join(not_starred)}."
        )

    return True, (
        "All 4 CEO-reporting contacts (Marcus Johnson, Diana Ross-Taylor, "
        "Carlos Mendoza, Sophia Andersson) are in VIP and starred."
    )
