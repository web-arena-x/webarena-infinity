import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    letters = state.get("patientLetters", [])
    for letter in letters:
        if letter.get("id") == "ltr_23":
            if letter.get("isRead") is True:
                return True, "Andrew McIntyre's message has been marked as read."
            else:
                return False, f"Letter ltr_23 found but isRead is {letter.get('isRead')}, expected True."

    return False, "Letter with id 'ltr_23' not found in patientLetters."
