import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    letters = state.get("patientLetters", [])
    letter = None
    for l in letters:
        if l.get("id") == "ltr_35":
            letter = l
            break

    if letter is None:
        return False, "Letter ltr_35 not found."

    if letter.get("isDraft") is True:
        return False, "Letter ltr_35 is still a draft."

    if letter.get("sentAt") is None:
        return False, "Letter ltr_35 has no sentAt timestamp."

    return True, "Draft letter to Martha Reeves-Whitfield has been sent."
