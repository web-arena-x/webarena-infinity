import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    patients = state.get("patients", [])
    patient_map = {p["id"]: p for p in patients}

    # Check pat_10 (Helen Matsumoto) sharing level
    pat_10 = patient_map.get("pat_10")
    if pat_10 is None:
        return False, "Patient pat_10 (Helen Matsumoto) not found in state."

    sharing_level = pat_10.get("passportSharingLevel")
    if sharing_level != 4:
        return False, (
            f"Helen Matsumoto's passportSharingLevel is {sharing_level}, expected 4."
        )

    # Check for a new to_patient letter with subject "Updated Passport Sharing Level"
    letters = state.get("patientLetters", [])
    expected_subject = "Updated Passport Sharing Level"

    notification_letter = next(
        (
            l for l in letters
            if l.get("patientId") == "pat_10"
            and l.get("subject") == expected_subject
            and l.get("direction") == "to_patient"
        ),
        None,
    )

    if notification_letter is None:
        return False, (
            f"No letter found for pat_10 with subject '{expected_subject}'."
        )

    if notification_letter.get("isDraft") is True:
        return False, (
            "Notification letter for Helen Matsumoto is still a draft, expected sent."
        )

    return True, "Helen Matsumoto's sharing level updated and notification letter sent."
