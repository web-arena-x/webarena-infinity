import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify 'Care-Coordination' tag on every patient with a signed note tagged 'Chronic-Care'."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    patients = state.get("patients", [])
    visit_notes = state.get("visitNotes", [])

    if not patients:
        return False, "No patients found in state"
    if not visit_notes:
        return False, "No visitNotes found in state"

    errors = []
    tag_name = "Care-Coordination"
    doc_tag = "Chronic-Care"

    # Find patients who have a signed note with "Chronic-Care" document tag
    patients_with_chronic_care = set()
    for note in visit_notes:
        if note.get("status", "").lower() == "signed":
            doc_tags = [dt.lower() for dt in note.get("documentTags", [])]
            if doc_tag.lower() in doc_tags:
                patients_with_chronic_care.add(note.get("patientId"))

    for patient in patients:
        patient_id = patient.get("id", "")
        patient_name = patient.get("lastName", patient.get("name", "unknown"))
        tags = [t.lower() for t in patient.get("tags", [])]
        has_tag = tag_name.lower() in tags

        if patient_id in patients_with_chronic_care and not has_tag:
            errors.append(
                f"Patient '{patient_name}' has a signed note tagged '{doc_tag}' but is missing '{tag_name}' tag"
            )
        elif patient_id not in patients_with_chronic_care and has_tag:
            errors.append(
                f"Patient '{patient_name}' has no signed note tagged '{doc_tag}' but has '{tag_name}' tag"
            )

    if errors:
        return False, "; ".join(errors)
    return True, "Care-Coordination tag correctly applied to patients with signed Chronic-Care notes"
