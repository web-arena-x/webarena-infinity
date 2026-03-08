import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Lowest O2 patient WITH a care plan gets 'Respiratory-Priority' + signed Problem-Focused note
    with Urgent Visit category, HPI and Assessment blocks."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Find patients with care plans
    care_plan_pids = {cp["patientId"] for cp in state.get("carePlans", [])}

    # Find lowest O2 among patients with care plans
    min_o2 = None
    min_o2_pid = None
    for v in state.get("vitals", []):
        o2 = v.get("oxygenSaturation")
        pid = v["patientId"]
        if o2 is not None and pid in care_plan_pids:
            if min_o2 is None or o2 < min_o2:
                min_o2 = o2
                min_o2_pid = pid

    if not min_o2_pid:
        return False, "No vitals with O2 found for patients with care plans."

    patient = next(
        (p for p in state["patients"] if p["id"] == min_o2_pid), None
    )
    if not patient:
        return False, f"Patient {min_o2_pid} not found."

    errors = []

    # Check tag
    if "Respiratory-Priority" not in patient.get("tags", []):
        errors.append(f"{patient['lastName']} missing 'Respiratory-Priority' tag.")

    # Find Problem-Focused template and Urgent Visit category
    pf_tmpl_id = None
    for t in state.get("visitNoteTemplates", []):
        if "problem-focused" in t.get("name", "").lower():
            pf_tmpl_id = t["id"]
            break

    urgent_cat_id = None
    for c in state.get("visitNoteCategories", []):
        if c.get("name") == "Urgent Visit":
            urgent_cat_id = c["id"]
            break

    # Check new signed note
    seed_note_ids = {
        "note_001", "note_002", "note_003", "note_004", "note_005",
        "note_006", "note_007", "note_008", "note_009", "note_010",
        "note_011", "note_012", "note_hist_001",
    }
    new_notes = [
        n for n in state.get("visitNotes", [])
        if n["patientId"] == min_o2_pid and n["id"] not in seed_note_ids
    ]
    matching = [
        n for n in new_notes
        if n.get("templateUsed") == pf_tmpl_id
        and n.get("category") == urgent_cat_id
        and n.get("status") == "signed"
    ]
    if not matching:
        errors.append(
            f"{patient['lastName']} missing signed note with Problem-Focused template "
            f"and Urgent Visit category."
        )
    else:
        note = matching[0]
        block_types = [b.get("type", "").lower() for b in note.get("blocks", [])]
        if "hpi" not in block_types:
            errors.append("Note missing HPI block.")
        if "assessment" not in block_types:
            errors.append("Note missing Assessment block.")

    if errors:
        return False, " ".join(errors)
    return True, (
        f"{patient['lastName']} (lowest O2 {min_o2}% with care plan) has "
        f"'Respiratory-Priority' tag and signed Problem-Focused Urgent Visit note."
    )
