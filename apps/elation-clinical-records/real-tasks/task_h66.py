import requests


def verify(server_url: str) -> tuple[bool, str]:
    """New 'Anxiety Management' template with HPI+Assessment+billing 99213.
    Nakamura signed note with that template + Telehealth category + Psychological Status block."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Check template exists
    tmpl = None
    for t in state.get("visitNoteTemplates", []):
        if t.get("name", "").lower() == "anxiety management":
            tmpl = t
            break
    if not tmpl:
        return False, "Template 'Anxiety Management' not found."

    content = tmpl.get("content", {})
    if not content.get("hpi"):
        errors.append("Template missing HPI section.")
    if not content.get("assessment"):
        errors.append("Template missing Assessment section.")

    billing = tmpl.get("billingItems", [])
    has_99213 = any(b.get("cptCode") == "99213" for b in billing)
    if not has_99213:
        errors.append("Template missing billing code 99213.")

    # Find Nakamura
    nakamura = None
    for p in state.get("patients", []):
        if p.get("lastName") == "Nakamura":
            nakamura = p
            break
    if not nakamura:
        return False, "Patient Nakamura not found."

    # Find Telehealth category
    tele_cat_id = None
    for c in state.get("visitNoteCategories", []):
        if c.get("name", "").lower() == "telehealth":
            tele_cat_id = c["id"]
            break

    # Find new note for Nakamura
    seed_note_ids = {
        "note_001", "note_002", "note_003", "note_004", "note_005",
        "note_006", "note_007", "note_008", "note_009", "note_010",
        "note_011", "note_012", "note_hist_001",
    }
    new_notes = [
        n for n in state.get("visitNotes", [])
        if n["patientId"] == nakamura["id"] and n["id"] not in seed_note_ids
    ]

    matching = None
    for n in new_notes:
        if tmpl and n.get("templateUsed") == tmpl["id"] and n.get("category") == tele_cat_id:
            matching = n
            break

    if not matching:
        errors.append("Nakamura missing new note with Anxiety Management template and Telehealth category.")
    else:
        blocks = matching.get("blocks", [])
        block_types = [b.get("type", "").lower() for b in blocks]
        if "psychological_status" not in block_types:
            errors.append("Note missing Psychological Status block.")
        if matching.get("status") != "signed":
            errors.append(f"Note status is '{matching.get('status')}', expected 'signed'.")

    if errors:
        return False, " ".join(errors)
    return True, (
        f"'Anxiety Management' template created. Nakamura has signed note "
        f"with Telehealth category, template, and Psychological Status block."
    )
