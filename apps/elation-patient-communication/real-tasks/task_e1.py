import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that Janet Okonkwo's message about her blood sugar is marked as read."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    letters = state.get("patientLetters", [])
    letter = None
    for ltr in letters:
        if ltr.get("id") == "ltr_20":
            letter = ltr
            break

    if letter is None:
        return False, "Letter ltr_20 (Janet Okonkwo's blood sugar message) not found in patientLetters"

    if not letter.get("isRead"):
        return False, f"Letter ltr_20 isRead is {letter.get('isRead')}, expected True"

    if letter.get("readAt") is None:
        return False, "Letter ltr_20 readAt is None, expected a timestamp"

    return True, "Janet Okonkwo's blood sugar message (ltr_20) is marked as read"
