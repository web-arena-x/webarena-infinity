import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Patients sharing Kowalski's anxiety ICD-10 (F41.1) each get a signed Telehealth visit note."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Find Kowalski's anxiety ICD-10
    kowalski = None
    for p in state.get("patients", []):
        if p.get("lastName") == "Kowalski":
            kowalski = p
            break
    if not kowalski:
        return False, "Patient Kowalski not found."

    anxiety_icd = None
    for prob in state.get("problems", []):
        if prob["patientId"] == kowalski["id"] and "anxiety" in prob.get("title", "").lower():
            anxiety_icd = prob.get("icd10")
            break
    if not anxiety_icd:
        return False, "Kowalski's anxiety diagnosis not found."

    # Find all patients with that ICD-10
    target_pids = set()
    for prob in state.get("problems", []):
        if prob.get("icd10") == anxiety_icd:
            target_pids.add(prob["patientId"])

    if len(target_pids) < 2:
        return False, f"Expected at least 2 patients with {anxiety_icd}, found {len(target_pids)}."

    # Find Telehealth category ID
    telehealth_cat_id = None
    for cat in state.get("visitNoteCategories", []):
        if cat.get("name", "").lower() == "telehealth":
            telehealth_cat_id = cat["id"]
            break
    if not telehealth_cat_id:
        return False, "Telehealth category not found."

    # Existing note IDs (seed data)
    seed_note_ids = {
        "note_001", "note_002", "note_003", "note_004", "note_005",
        "note_006", "note_007", "note_008", "note_009", "note_010",
        "note_011", "note_012", "note_hist_001",
    }

    errors = []
    for pid in target_pids:
        patient_name = next(
            (p["lastName"] for p in state["patients"] if p["id"] == pid), pid
        )
        new_notes = [
            n for n in state.get("visitNotes", [])
            if n["patientId"] == pid and n["id"] not in seed_note_ids
        ]
        matching = [
            n for n in new_notes
            if n.get("category") == telehealth_cat_id and n.get("status") == "signed"
        ]
        if not matching:
            errors.append(
                f"{patient_name} is missing a new signed Telehealth visit note."
            )

    if errors:
        return False, " ".join(errors)
    return True, f"All {len(target_pids)} patients with {anxiety_icd} have signed Telehealth notes."
