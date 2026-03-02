import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Patients with "Diabetes Management" tag:
    # pat_1 (James Rodriguez), pat_11 (Kevin Adebayo),
    # pat_30 (Janet Okonkwo), pat_35 (Raymond Copeland)
    target_patients = {
        "pat_1": "James Rodriguez",
        "pat_11": "Kevin Adebayo",
        "pat_30": "Janet Okonkwo",
        "pat_35": "Raymond Copeland",
    }

    expected_subject = "Annual A1C Screening Reminder"

    # Check for bulk letter
    bulk_letters = state.get("bulkLetters", [])
    matching_bulk = [
        bl for bl in bulk_letters
        if bl.get("subject") == expected_subject
    ]
    if not matching_bulk:
        return False, (
            f"No bulk letter found with subject '{expected_subject}'."
        )

    # Check individual patient letters
    letters = state.get("patientLetters", [])
    missing_patients = []

    for pid, name in target_patients.items():
        patient_letter = next(
            (
                l for l in letters
                if l.get("patientId") == pid
                and l.get("subject") == expected_subject
                and l.get("direction") == "to_patient"
            ),
            None,
        )
        if patient_letter is None:
            missing_patients.append(f"{name} ({pid})")

    if missing_patients:
        return False, (
            f"Missing patient letters for: {', '.join(missing_patients)}."
        )

    return True, "Bulk letter sent to all 4 Diabetes Management patients."
