import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    patients = state.get("patients", [])
    patient = None
    for p in patients:
        if p.get("firstName") == "Anthony" and p.get("lastName") == "Petrov":
            patient = p
            break

    if patient is None:
        return False, "Patient Anthony Petrov not found."

    if patient.get("passportStatus") != "invited":
        return False, f"Anthony Petrov's passport status is '{patient.get('passportStatus')}', expected 'invited'."

    if patient.get("invitedAt") is None:
        return False, "Anthony Petrov's invitedAt is not set."

    if patient.get("invitationCode") is None:
        return False, "Anthony Petrov's invitationCode is not set."

    return True, "Anthony Petrov has been invited to Passport."
