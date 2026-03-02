import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    patients = state.get("patients", [])
    patient = None
    for p in patients:
        if p.get("firstName") == "Brian" and p.get("lastName") == "Murphy":
            patient = p
            break

    if patient is None:
        return False, "Patient Brian Murphy not found."

    if patient.get("passportStatus") != "invited":
        return False, f"Brian Murphy's passport status is '{patient.get('passportStatus')}', expected 'invited'."

    if patient.get("passportSharingLevel") != 3:
        return False, f"Brian Murphy's sharing level is {patient.get('passportSharingLevel')}, expected 3."

    if patient.get("invitationCode") is None:
        return False, "Brian Murphy's invitationCode is not set."

    return True, "Brian Murphy invited to Passport with sharing level 3."
