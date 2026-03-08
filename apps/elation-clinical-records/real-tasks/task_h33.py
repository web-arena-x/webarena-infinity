import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify 'Respiratory-Alert' tag on every patient with an active problem whose ICD-10 starts with J."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    patients = state.get("patients", [])
    problems = state.get("problems", [])

    if not patients:
        return False, "No patients found in state"
    if not problems:
        return False, "No problems found in state"

    errors = []
    tag_name = "Respiratory-Alert"

    # Determine which patients should have the tag
    patients_with_j_code = set()
    for prob in problems:
        if prob.get("status", "").lower() == "active":
            icd = prob.get("icd10", "")
            if icd.upper().startswith("J"):
                patients_with_j_code.add(prob.get("patientId"))

    for patient in patients:
        patient_id = patient.get("id", "")
        patient_name = patient.get("lastName", patient.get("name", "unknown"))
        tags = [t.lower() for t in patient.get("tags", [])]
        has_tag = tag_name.lower() in tags

        if patient_id in patients_with_j_code and not has_tag:
            errors.append(
                f"Patient '{patient_name}' has an active problem with J-code but is missing '{tag_name}' tag"
            )
        elif patient_id not in patients_with_j_code and has_tag:
            errors.append(
                f"Patient '{patient_name}' has no active J-code problem but has '{tag_name}' tag"
            )

    if errors:
        return False, "; ".join(errors)
    return True, "Respiratory-Alert tag correctly applied to patients with active J-code problems"
