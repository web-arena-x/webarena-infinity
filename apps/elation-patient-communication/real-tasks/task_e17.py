import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that the draft letter to Martha Reeves-Whitfield (ltr_35) has been sent."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    letters = state.get("patientLetters", [])
    letter = None
    for ltr in letters:
        if ltr.get("id") == "ltr_35":
            letter = ltr
            break

    if letter is None:
        return False, "Letter ltr_35 (draft to Martha Reeves-Whitfield) not found in patientLetters"

    if letter.get("isDraft") is not False:
        return False, f"Letter ltr_35 isDraft is {letter.get('isDraft')}, expected False"

    if letter.get("sentAt") is None:
        return False, "Letter ltr_35 sentAt is None, expected a timestamp"

    return True, "Draft letter to Martha Reeves-Whitfield (ltr_35) has been sent"
