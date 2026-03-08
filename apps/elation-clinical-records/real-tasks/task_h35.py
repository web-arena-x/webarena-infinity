import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Find Fitzgerald (pat_011)
    patients = state.get("patients", [])
    fitzgerald = None
    for p in patients:
        if p.get("lastName") == "Fitzgerald":
            fitzgerald = p
            break
    if not fitzgerald:
        return False, "Patient with lastName 'Fitzgerald' not found."

    patient_id = fitzgerald.get("id", "pat_011")

    # Check vitals for Fitzgerald
    vitals = state.get("vitals", [])
    fitz_vitals = [v for v in vitals if v.get("patientId") == patient_id]

    if not fitz_vitals:
        return False, "No vitals entry found for Fitzgerald."

    expected = {
        "bloodPressureSystolic": 122,
        "bloodPressureDiastolic": 76,
        "heartRate": 68,
        "temperature": 98.4,
        "oxygenSaturation": 99,
        "weight": 180,
        "height": 72,
        "painLevel": 0,
    }

    vitals_ok = False
    vitals_errors = []
    for entry in fitz_vitals:
        entry_errors = []
        for field, expected_val in expected.items():
            actual = entry.get(field)
            if actual is None:
                entry_errors.append(f"{field} is missing")
            elif float(actual) != float(expected_val):
                entry_errors.append(f"{field}={actual}, expected {expected_val}")
        if not entry_errors:
            vitals_ok = True
            break
        vitals_errors.append(
            f"id={entry.get('id', '?')}: {', '.join(entry_errors)}"
        )

    if not vitals_ok:
        return False, (
            f"No vitals entry for Fitzgerald matches expected values. "
            f"Found {len(fitz_vitals)} entry/entries: {'; '.join(vitals_errors)}"
        )

    # Check for a new visit note with templateUsed tmpl_002 and category cat_001
    notes = state.get("visitNotes", [])
    fitz_notes = [n for n in notes if n.get("patientId") == patient_id]

    if not fitz_notes:
        return False, "No visit note found for Fitzgerald."

    for note in fitz_notes:
        template = note.get("templateUsed")
        category = note.get("category")
        if template == "tmpl_002" and category == "cat_001":
            return True, (
                f"Fitzgerald has vitals with correct values and a visit note "
                f"(id={note.get('id')}) with templateUsed=tmpl_002 and category=cat_001."
            )

    # Diagnostics
    details = []
    for note in fitz_notes:
        details.append(
            f"id={note.get('id')}: templateUsed={note.get('templateUsed')}, "
            f"category={note.get('category')}"
        )
    return False, (
        f"Fitzgerald has vitals but no visit note with templateUsed=tmpl_002 and "
        f"category=cat_001. Found {len(fitz_notes)} note(s): {'; '.join(details)}"
    )
