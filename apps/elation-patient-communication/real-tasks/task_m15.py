import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that a message about spirometry has been sent to David Park with no reply allowed."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    # Find David Park's patient ID
    patients = state.get("patients", [])
    patient_id = None
    for pat in patients:
        if pat.get("firstName") == "David" and pat.get("lastName") == "Park":
            patient_id = pat.get("id")
            break

    if patient_id is None:
        return False, "Patient David Park not found"

    # Known seed letter IDs that existed before the task (ltr_1 through ltr_47)
    seed_letter_ids = {f"ltr_{i}" for i in range(1, 48)}

    letters = state.get("patientLetters", [])
    matching_letter = None
    for ltr in letters:
        if (ltr.get("patientId") == patient_id
                and ltr.get("direction") == "to_patient"
                and ltr.get("id") not in seed_letter_ids):
            # Check if subject or body mentions spirometry
            subject = (ltr.get("subject") or "").lower()
            body = (ltr.get("body") or "").lower()
            if "spirometry" in subject or "spirometry" in body:
                matching_letter = ltr
                break

    if matching_letter is None:
        return False, (
            "No new letter to David Park mentioning 'spirometry' found in patientLetters"
        )

    if matching_letter.get("doNotAllowResponse") is not True:
        return False, (
            f"Letter {matching_letter.get('id')} doNotAllowResponse is "
            f"{matching_letter.get('doNotAllowResponse')}, expected True"
        )

    if matching_letter.get("isDraft") is True:
        return False, (
            f"Letter {matching_letter.get('id')} isDraft is True, expected False (message should be sent)"
        )

    return True, "Message about spirometry sent to David Park with doNotAllowResponse=True"
