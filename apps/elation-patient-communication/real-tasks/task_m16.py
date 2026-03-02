import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Check letter ltr_20 is read
    letters = state.get("patientLetters", [])
    letter = None
    for l in letters:
        if l.get("id") == "ltr_20":
            letter = l
            break

    if letter is None:
        return False, "Letter ltr_20 not found."

    if letter.get("isRead") is not True:
        return False, "Letter ltr_20 (Janet Okonkwo's message) is not marked as read."

    # Check patient pat_30 has High Risk tag
    patients = state.get("patients", [])
    patient = None
    for p in patients:
        if p.get("id") == "pat_30":
            patient = p
            break

    if patient is None:
        return False, "Patient pat_30 (Janet Okonkwo) not found."

    tags = patient.get("tags", [])
    if "High Risk" not in tags:
        return False, f"'High Risk' tag not found on Janet Okonkwo. Current tags: {tags}."

    return True, "Janet Okonkwo's message marked as read and tagged as High Risk."
