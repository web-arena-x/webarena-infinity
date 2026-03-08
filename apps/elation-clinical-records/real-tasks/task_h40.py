import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    patients = state.get("patients", [])
    notes = state.get("visitNotes", [])

    if not patients:
        return False, "No patients found in state."

    # Build set of patient IDs that have at least one visit note
    patients_with_notes = set()
    for n in notes:
        pid = n.get("patientId")
        if pid:
            patients_with_notes.add(pid)

    tag_name = "Needs-Visit"
    errors = []

    for patient in patients:
        patient_id = patient.get("id", "")
        last_name = patient.get("lastName", "?")
        tags = patient.get("tags", [])
        has_tag = tag_name in tags
        has_notes = patient_id in patients_with_notes

        if not has_notes and not has_tag:
            errors.append(
                f"{last_name} ({patient_id}) has no visit notes but is missing "
                f"'{tag_name}' tag. Current tags: {tags}"
            )
        elif has_notes and has_tag:
            errors.append(
                f"{last_name} ({patient_id}) has visit notes but was incorrectly "
                f"given '{tag_name}' tag (over-tagging). Current tags: {tags}"
            )

    if errors:
        return False, "; ".join(errors)

    return True, (
        "All patients without visit notes (Sharma, Fitzgerald, Wu) have "
        "'Needs-Visit' tag, and no patients with notes have the tag."
    )
