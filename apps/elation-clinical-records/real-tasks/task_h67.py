import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Most recent vaccination patient gets 'Recent-Immunization' tag + signed Follow-Up note with HTN template."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Find patient with most recent vaccination
    most_recent_vax = None
    for v in state.get("vaccinations", []):
        given = v.get("givenOn", "")
        if given and (most_recent_vax is None or given > most_recent_vax.get("givenOn", "")):
            most_recent_vax = v

    if not most_recent_vax:
        return False, "No vaccinations found."

    target_pid = most_recent_vax["patientId"]
    patient = None
    for p in state.get("patients", []):
        if p["id"] == target_pid:
            patient = p
            break
    if not patient:
        return False, f"Patient {target_pid} not found."

    errors = []

    # Check tag
    if "Recent-Immunization" not in patient.get("tags", []):
        errors.append(f"{patient['lastName']} missing 'Recent-Immunization' tag.")

    # Find Follow-Up category and Hypertension Follow-Up template
    followup_cat_id = None
    for c in state.get("visitNoteCategories", []):
        if c.get("name") == "Follow-Up":
            followup_cat_id = c["id"]
            break

    htn_tmpl_id = None
    for t in state.get("visitNoteTemplates", []):
        if "hypertension" in t.get("name", "").lower() and "follow" in t.get("name", "").lower():
            htn_tmpl_id = t["id"]
            break

    # Check new signed note
    seed_note_ids = {
        "note_001", "note_002", "note_003", "note_004", "note_005",
        "note_006", "note_007", "note_008", "note_009", "note_010",
        "note_011", "note_012", "note_hist_001",
    }
    new_notes = [
        n for n in state.get("visitNotes", [])
        if n["patientId"] == target_pid and n["id"] not in seed_note_ids
    ]
    matching = [
        n for n in new_notes
        if n.get("category") == followup_cat_id
        and n.get("templateUsed") == htn_tmpl_id
        and n.get("status") == "signed"
    ]
    if not matching:
        errors.append(
            f"{patient['lastName']} missing signed Follow-Up note with "
            f"Hypertension Follow-Up template."
        )

    if errors:
        return False, " ".join(errors)
    return True, (
        f"{patient['lastName']} (most recent vax) has 'Recent-Immunization' tag "
        f"and signed Follow-Up note with Hypertension Follow-Up template."
    )
