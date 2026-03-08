import requests


def verify(server_url: str) -> tuple[bool, str]:
    """New 'Comprehensive Review' category with MIPS. New 'Full Review' template with
    HPI+ROS+PE+Assessment + billing 99215. Annual Exam appointment uses both.
    Zhao has signed note with both."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Check category
    new_cat = None
    for c in state.get("visitNoteCategories", []):
        if c.get("name", "").lower() == "comprehensive review":
            new_cat = c
            break
    if not new_cat:
        return False, "Category 'Comprehensive Review' not found."
    if not new_cat.get("countForMIPS"):
        errors.append("'Comprehensive Review' should have MIPS enabled.")

    # Check template
    new_tmpl = None
    for t in state.get("visitNoteTemplates", []):
        if t.get("name", "").lower() == "full review":
            new_tmpl = t
            break
    if not new_tmpl:
        return False, "Template 'Full Review' not found."

    content = new_tmpl.get("content", {})
    for section in ["hpi", "ros", "pe", "assessment"]:
        if not content.get(section):
            errors.append(f"Template 'Full Review' missing {section} section.")

    billing = new_tmpl.get("billingItems", [])
    if not any(b.get("cptCode") == "99215" for b in billing):
        errors.append("Template missing billing code 99215.")

    # Check Annual Exam appointment
    annual = None
    for apt in state.get("appointmentTypes", []):
        if apt.get("name") == "Annual Exam":
            annual = apt
            break
    if not annual:
        errors.append("Annual Exam appointment not found.")
    else:
        if new_tmpl and annual.get("noteTemplate") != new_tmpl["id"]:
            errors.append(
                f"Annual Exam template should be '{new_tmpl['id']}', "
                f"got '{annual.get('noteTemplate')}'."
            )
        if new_cat and annual.get("noteCategory") != new_cat["id"]:
            errors.append(
                f"Annual Exam category should be '{new_cat['id']}', "
                f"got '{annual.get('noteCategory')}'."
            )

    # Check Zhao's signed note
    zhao = None
    for p in state.get("patients", []):
        if p.get("lastName") == "Zhao":
            zhao = p
            break
    if not zhao:
        errors.append("Patient Zhao not found.")
    else:
        seed_note_ids = {
            "note_001", "note_002", "note_003", "note_004", "note_005",
            "note_006", "note_007", "note_008", "note_009", "note_010",
            "note_011", "note_012", "note_hist_001",
        }
        new_notes = [
            n for n in state.get("visitNotes", [])
            if n["patientId"] == zhao["id"] and n["id"] not in seed_note_ids
        ]
        matching = [
            n for n in new_notes
            if new_tmpl and n.get("templateUsed") == new_tmpl["id"]
            and new_cat and n.get("category") == new_cat["id"]
            and n.get("status") == "signed"
        ]
        if not matching:
            errors.append(
                "Zhao missing signed note with 'Full Review' template "
                "and 'Comprehensive Review' category."
            )

    if errors:
        return False, " ".join(errors)
    return True, (
        "'Comprehensive Review' category and 'Full Review' template created. "
        "Annual Exam appointment configured. Zhao has signed note."
    )
