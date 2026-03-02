import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    priya_id = "user_5"
    kevin_id = "user_6"

    matters = state.get("matters", [])

    # Check no matter is still assigned to Priya Sharma
    priya_matters = [
        m for m in matters if m.get("responsibleAttorneyId") == priya_id
    ]

    if priya_matters:
        priya_descriptions = [
            f"{m.get('id')} ('{m.get('description', '')}')" for m in priya_matters
        ]
        errors.append(
            f"{len(priya_matters)} matter(s) still assigned to Priya Sharma (user_5): "
            f"{', '.join(priya_descriptions[:5])}."
        )

    # Check Kevin Nakamura has at least 8 matters
    kevin_matters = [
        m for m in matters if m.get("responsibleAttorneyId") == kevin_id
    ]

    if len(kevin_matters) < 8:
        errors.append(
            f"Kevin Nakamura (user_6) has {len(kevin_matters)} matter(s), expected at least 8."
        )

    # Verify known Priya matters are now with Kevin
    known_priya_matter_ids = [
        "matter_10", "matter_12", "matter_16", "matter_18", "matter_22",
        "matter_25", "matter_48", "matter_49", "matter_51", "matter_53", "matter_106"
    ]
    matters_by_id = {m.get("id"): m for m in matters}

    transferred_count = 0
    for mid in known_priya_matter_ids:
        matter = matters_by_id.get(mid)
        if matter is None:
            continue
        if matter.get("responsibleAttorneyId") == kevin_id:
            transferred_count += 1

    if transferred_count < 8:
        errors.append(
            f"Only {transferred_count} of Priya Sharma's known matters were transferred to "
            f"Kevin Nakamura, expected at least 8."
        )

    if errors:
        return False, "Transfer of Priya Sharma's matters to Kevin Nakamura incomplete. " + " | ".join(errors)

    return True, (
        f"All of Priya Sharma's matters have been transferred to Kevin Nakamura. "
        f"Kevin now has {len(kevin_matters)} matter(s) and {transferred_count} known transfers confirmed."
    )
