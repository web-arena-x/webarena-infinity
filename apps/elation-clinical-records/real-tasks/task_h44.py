import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Look up Flu Shot appointment template → create note for Washington with that template + Vaccination Only category."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Find Flu Shot appointment type and its template
    flu_apt = None
    for a in state.get("appointmentTypes", []):
        if a.get("name", "").lower() == "flu shot":
            flu_apt = a
            break
    if not flu_apt:
        return False, "Flu Shot appointment type not found."
    expected_tmpl = flu_apt.get("noteTemplate", "")
    if not expected_tmpl:
        return False, "Flu Shot appointment type has no template assigned."

    # Find Vaccination Only category
    vax_cat_id = None
    for c in state.get("visitNoteCategories", []):
        if c.get("name", "").lower() == "vaccination only":
            vax_cat_id = c.get("id")
            break
    if not vax_cat_id:
        return False, "Vaccination Only category not found."

    # Find Aaliyah Washington
    washington = None
    for p in state.get("patients", []):
        if p.get("lastName") == "Washington":
            washington = p
            break
    if not washington:
        return False, "Patient Washington not found."

    # Check for new note
    existing_note_ids = {"note_008"}  # Washington's existing note
    patient_notes = [
        n for n in state.get("visitNotes", [])
        if n.get("patientId") == washington["id"] and n.get("id") not in existing_note_ids
    ]

    matching_note = None
    for n in patient_notes:
        cat = n.get("category") or n.get("categoryId", "")
        tmpl = n.get("templateUsed", "")
        if cat == vax_cat_id and tmpl == expected_tmpl:
            matching_note = n
            break

    if not matching_note:
        return False, (
            f"Washington does not have a new visit note with Vaccination Only category "
            f"and template {expected_tmpl}."
        )

    return True, (
        f"Washington has a new visit note (id={matching_note['id']}) "
        f"with Vaccination Only category and template={expected_tmpl}."
    )
