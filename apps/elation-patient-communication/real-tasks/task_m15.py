import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    patients = state.get("patients", [])
    patient = None
    for p in patients:
        if p.get("firstName") == "Patricia" and (
            p.get("lastName") == "O'Brien"
            or p.get("lastName") == "O\\'Brien"
            or "Brien" in str(p.get("lastName", ""))
        ):
            patient = p
            break

    # Fallback: try by known id
    if patient is None:
        for p in patients:
            if p.get("id") == "pat_8":
                patient = p
                break

    if patient is None:
        return False, "Patient Patricia O'Brien (pat_8) not found."

    if patient.get("passportAccountDisabled") is not True:
        return False, f"Patricia O'Brien's passportAccountDisabled is {patient.get('passportAccountDisabled')}, expected True."

    if patient.get("passportStatus") != "not_invited":
        return False, f"Patricia O'Brien's passportStatus is '{patient.get('passportStatus')}', expected 'not_invited'."

    return True, "Patricia O'Brien's Passport access has been revoked."
