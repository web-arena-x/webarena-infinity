import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    patients = state.get("patients", [])
    patient_map = {p["id"]: p for p in patients}

    pat_3 = patient_map.get("pat_3")
    if pat_3 is None:
        return False, "Patient pat_3 (Robert Washington) not found in state."

    # Check Passport account is disabled
    if pat_3.get("passportAccountDisabled") is not True:
        return False, (
            "Robert Washington's passportAccountDisabled is not True."
        )

    # Check passport status is not_invited
    if pat_3.get("passportStatus") != "not_invited":
        return False, (
            f"Robert Washington's passportStatus is "
            f"'{pat_3.get('passportStatus')}', expected 'not_invited'."
        )

    # Check tags are empty
    tags = pat_3.get("tags", [])
    if tags != [] and tags != list():
        return False, (
            f"Robert Washington still has tags: {tags}. Expected empty list."
        )

    return True, "Robert Washington's Passport disabled and all tags removed."
