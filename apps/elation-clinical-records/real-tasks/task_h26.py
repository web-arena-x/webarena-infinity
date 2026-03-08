import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Check 1: Category "Geriatric Care" exists with countForMIPS=true
    categories = state.get("visitNoteCategories", [])
    geriatric_care_cat = None
    for cat in categories:
        name = (cat.get("name") or "").strip()
        if name.lower() == "geriatric care":
            geriatric_care_cat = cat
            break

    if not geriatric_care_cat:
        cat_names = [c.get("name") for c in categories]
        return False, f"Category 'Geriatric Care' not found. Current categories: {cat_names}"

    if not geriatric_care_cat.get("countForMIPS"):
        errors.append(
            f"Category 'Geriatric Care' (id={geriatric_care_cat.get('id')}) has "
            f"countForMIPS={geriatric_care_cat.get('countForMIPS')}, expected true"
        )

    geriatric_care_id = geriatric_care_cat.get("id")

    # Find Zhao (pat_010)
    patients = state.get("patients", [])
    zhao = None
    for p in patients:
        if p.get("lastName") == "Zhao":
            zhao = p
            break
    if not zhao:
        return False, "Patient with lastName 'Zhao' not found."

    patient_id = zhao.get("id", "pat_010")

    # Check 2: New visit note for Zhao with the Geriatric Care category and tmpl_001
    existing_note_ids = {"note_010"}
    notes = state.get("visitNotes", [])
    zhao_new_notes = [
        n for n in notes
        if n.get("patientId") == patient_id and n.get("id") not in existing_note_ids
    ]

    if not zhao_new_notes:
        errors.append("No new visit note found for Zhao (existing note_010 excluded).")
        return False, "; ".join(errors)

    # Find a note matching the criteria
    matching_note = None
    for note in zhao_new_notes:
        category = note.get("categoryId") or note.get("category")
        template = note.get("templateUsed")
        if category == geriatric_care_id and template == "tmpl_001":
            matching_note = note
            break

    if not matching_note:
        details = []
        for note in zhao_new_notes:
            cat = note.get("categoryId") or note.get("category")
            tmpl = note.get("templateUsed")
            status = note.get("status")
            details.append(f"id={note.get('id')}: categoryId={cat}, templateUsed={tmpl}, status={status}")
        errors.append(
            f"Found {len(zhao_new_notes)} new note(s) for Zhao but none have "
            f"categoryId='{geriatric_care_id}' and templateUsed='tmpl_001'. "
            f"Details: {'; '.join(details)}"
        )
        return False, "; ".join(errors)

    # Check 3: The note must be signed
    note_status = matching_note.get("status", "")
    if note_status != "signed":
        errors.append(
            f"Zhao's new note (id={matching_note.get('id')}) has status '{note_status}', "
            f"expected 'signed'"
        )

    if errors:
        return False, "; ".join(errors)

    return True, (
        f"Category 'Geriatric Care' (id={geriatric_care_id}) exists with MIPS enabled. "
        f"Zhao has a signed visit note (id={matching_note.get('id')}) with that category "
        f"and Annual Wellness Visit template (tmpl_001)."
    )
