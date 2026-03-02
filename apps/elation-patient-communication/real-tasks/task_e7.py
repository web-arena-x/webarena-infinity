import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    letters = state.get("patientLetters", [])
    for letter in letters:
        if letter.get("id") == "ltr_35":
            return False, "Draft letter ltr_35 to Martha Reeves-Whitfield still exists in patientLetters."

    return True, "Draft letter to Martha Reeves-Whitfield has been deleted."
