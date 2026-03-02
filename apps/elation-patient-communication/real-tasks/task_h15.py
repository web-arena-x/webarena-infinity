import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    letters = state.get("patientLetters", [])
    letter_map = {l["id"]: l for l in letters}

    # Unread letters from Dr. Chen's (prov_1) patients in seed data
    prov1_unread_ids = [
        "ltr_4", "ltr_6", "ltr_10", "ltr_15", "ltr_19",
        "ltr_20", "ltr_24", "ltr_29", "ltr_47",
    ]

    # Check all prov_1 patient unread letters are now read
    for lid in prov1_unread_ids:
        ltr = letter_map.get(lid)
        if ltr is None:
            return False, f"Letter {lid} not found in state."
        if ltr.get("isRead") is not True:
            return False, (
                f"Letter {lid} (Dr. Chen's patient) is still unread."
            )

    # Check that unread letters from OTHER providers' patients remain unread
    other_provider_unread_ids = ["ltr_23", "ltr_39", "ltr_46"]

    for lid in other_provider_unread_ids:
        ltr = letter_map.get(lid)
        if ltr is None:
            continue  # May not exist
        if ltr.get("isRead") is True:
            return False, (
                f"Letter {lid} (not Dr. Chen's patient) was incorrectly "
                f"marked as read. Only Dr. Chen's patient messages should "
                f"have been marked."
            )

    return True, "All unread messages from Dr. Chen's patients have been marked as read."
