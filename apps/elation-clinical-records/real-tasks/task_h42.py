import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Patient with most recent Urgent Visit note → new signed note with Follow-Up category + Hypertension template."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Find the Urgent Visit category id
    urgent_cat_id = None
    for c in state.get("visitNoteCategories", []):
        if c.get("name", "").lower() == "urgent visit":
            urgent_cat_id = c.get("id")
            break
    if not urgent_cat_id:
        return False, "Urgent Visit category not found."

    # Find patient with most recent note in Urgent Visit category
    urgent_notes = [
        n for n in state.get("visitNotes", [])
        if (n.get("category") == urgent_cat_id or n.get("categoryId") == urgent_cat_id)
    ]
    if not urgent_notes:
        return False, "No visit notes with Urgent Visit category found."

    urgent_notes.sort(key=lambda n: n.get("date", ""), reverse=True)
    target_pid = urgent_notes[0].get("patientId")
    existing_urgent_note_ids = {n.get("id") for n in urgent_notes}

    # Find patient name
    patient = None
    for p in state.get("patients", []):
        if p.get("id") == target_pid:
            patient = p
            break
    if not patient:
        return False, f"Patient {target_pid} not found."
    last_name = patient.get("lastName", "?")

    # Find Follow-Up category
    followup_cat_id = None
    for c in state.get("visitNoteCategories", []):
        if c.get("name", "").lower() == "follow-up":
            followup_cat_id = c.get("id")
            break
    if not followup_cat_id:
        return False, "Follow-Up category not found."

    # Find Hypertension Follow-Up template
    htn_tmpl_id = None
    for t in state.get("visitNoteTemplates", []):
        if "hypertension" in t.get("name", "").lower() and "follow" in t.get("name", "").lower():
            htn_tmpl_id = t.get("id")
            break
    if not htn_tmpl_id:
        return False, "Hypertension Follow-Up template not found."

    # Check for a new signed note for this patient with Follow-Up category and Hypertension template
    patient_notes = [
        n for n in state.get("visitNotes", [])
        if n.get("patientId") == target_pid and n.get("id") not in existing_urgent_note_ids
    ]

    matching_note = None
    for n in patient_notes:
        cat = n.get("category") or n.get("categoryId", "")
        tmpl = n.get("templateUsed", "")
        if cat == followup_cat_id and tmpl == htn_tmpl_id and n.get("status") == "signed":
            matching_note = n
            break

    if not matching_note:
        return False, (
            f"{last_name} does not have a new signed visit note with Follow-Up category "
            f"and Hypertension Follow-Up template."
        )

    return True, (
        f"{last_name} has a new signed visit note (id={matching_note['id']}) "
        f"with Follow-Up category and Hypertension Follow-Up template."
    )
