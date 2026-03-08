import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Confirm Johnson is the patient who declined a vaccination
    patients = state.get("patients", [])
    johnson = None
    for p in patients:
        if p.get("lastName") == "Johnson":
            johnson = p
            break
    if not johnson:
        return False, "Patient with lastName 'Johnson' not found."

    patient_id = johnson.get("id", "pat_003")

    # Verify Johnson actually has a declined vaccination
    vaccinations = state.get("vaccinations", [])
    declined = [
        v for v in vaccinations
        if v.get("patientId") == patient_id and v.get("recordType") == "Declined"
    ]
    if not declined:
        return False, "No declined vaccination found for Johnson — seed data may be wrong."

    # Find new visit notes for Johnson (exclude existing note_005, note_006)
    existing_note_ids = {"note_005", "note_006"}
    notes = state.get("visitNotes", [])
    johnson_new_notes = [
        n for n in notes
        if n.get("patientId") == patient_id and n.get("id") not in existing_note_ids
    ]

    if not johnson_new_notes:
        return False, "No new visit note found for Johnson (existing notes note_005, note_006 excluded)."

    # Check for a note with Telehealth category (cat_002)
    for note in johnson_new_notes:
        category = note.get("categoryId") or note.get("category")
        if category == "cat_002":
            return True, (
                f"New visit note for Johnson (id={note.get('id')}) with Telehealth category "
                f"(cat_002) found."
            )

    # Diagnostics
    details = []
    for note in johnson_new_notes:
        cat = note.get("categoryId") or note.get("category")
        details.append(f"id={note.get('id')}: categoryId={cat}")

    return False, (
        f"Found {len(johnson_new_notes)} new note(s) for Johnson but none have "
        f"categoryId='cat_002' (Telehealth). Details: {'; '.join(details)}"
    )
