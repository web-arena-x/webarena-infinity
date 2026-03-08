import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Duplicate Diabetes Management → 'Diabetes Annual Review' + billing 99395. Henderson note with it + Annual Exam."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Check duplicate template exists
    dup = None
    for t in state.get("visitNoteTemplates", []):
        if t.get("name") == "Diabetes Annual Review":
            dup = t
            break
    if not dup:
        return False, "Template 'Diabetes Annual Review' not found."

    # Should have HPI content from Diabetes Management
    content = dup.get("content", {})
    if not content.get("hpi"):
        errors.append("Duplicate template missing HPI section.")

    # Should have billing code 99395
    billing = dup.get("billingItems", [])
    has_99395 = any(b.get("cptCode") == "99395" for b in billing)
    if not has_99395:
        errors.append("Duplicate template missing billing code 99395.")

    # Find Henderson
    henderson = None
    for p in state.get("patients", []):
        if p.get("lastName") == "Henderson":
            henderson = p
            break
    if not henderson:
        return False, "Patient Henderson not found."

    # Check new note for Henderson with duplicate template and Annual Exam category
    annual_cat_id = None
    for c in state.get("visitNoteCategories", []):
        if c.get("name") == "Annual Exam":
            annual_cat_id = c["id"]
            break

    seed_note_ids = {
        "note_001", "note_002", "note_003", "note_004", "note_005",
        "note_006", "note_007", "note_008", "note_009", "note_010",
        "note_011", "note_012", "note_hist_001",
    }
    new_notes = [
        n for n in state.get("visitNotes", [])
        if n["patientId"] == henderson["id"] and n["id"] not in seed_note_ids
    ]
    matching = [
        n for n in new_notes
        if dup and n.get("templateUsed") == dup["id"] and n.get("category") == annual_cat_id
    ]
    if not matching:
        errors.append(
            "Henderson missing new note with 'Diabetes Annual Review' template "
            "and Annual Exam category."
        )

    if errors:
        return False, " ".join(errors)
    return True, (
        "'Diabetes Annual Review' template with 99395 billing created. "
        "Henderson has note with it in Annual Exam category."
    )
