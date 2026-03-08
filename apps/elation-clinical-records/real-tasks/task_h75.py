import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Patients with 'Pain' in problem title get 'Pain-Protocol' tag + new visit note."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Find patients with problems containing 'Pain'
    pain_pids = set()
    for prob in state.get("problems", []):
        if "pain" in prob.get("title", "").lower():
            pain_pids.add(prob["patientId"])

    # Find E* Problem-Focused template and Office Visit category
    pf_tmpl_id = None
    for t in state.get("visitNoteTemplates", []):
        if "problem-focused" in t.get("name", "").lower():
            pf_tmpl_id = t["id"]
            break

    ov_cat_id = None
    for c in state.get("visitNoteCategories", []):
        if c.get("name") == "Office Visit":
            ov_cat_id = c["id"]
            break

    seed_note_ids = {
        "note_001", "note_002", "note_003", "note_004", "note_005",
        "note_006", "note_007", "note_008", "note_009", "note_010",
        "note_011", "note_012", "note_hist_001",
    }

    errors = []
    for pid in pain_pids:
        patient = next((p for p in state["patients"] if p["id"] == pid), None)
        if not patient:
            continue
        name = patient.get("lastName", pid)

        # Check tag
        if "Pain-Protocol" not in patient.get("tags", []):
            errors.append(f"{name} missing 'Pain-Protocol' tag.")

        # Check new note with template + category
        new_notes = [
            n for n in state.get("visitNotes", [])
            if n["patientId"] == pid and n["id"] not in seed_note_ids
        ]
        matching = [
            n for n in new_notes
            if n.get("templateUsed") == pf_tmpl_id and n.get("category") == ov_cat_id
        ]
        if not matching:
            errors.append(
                f"{name} missing new note with Problem-Focused template "
                f"and Office Visit category."
            )

    if errors:
        return False, " ".join(errors)
    return True, f"{len(pain_pids)} patients with 'Pain' problems tagged and notes created."
