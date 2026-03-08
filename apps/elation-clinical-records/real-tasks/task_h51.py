import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Find patient with lowest SpO2 → create note with E* Problem-Focused template, add HPI + Assessment, sign."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Find patient with lowest SpO2 across most recent vitals per patient
    latest_vitals = {}
    for v in state.get("vitals", []):
        pid = v.get("patientId")
        spo2 = v.get("oxygenSaturation")
        if spo2 is None:
            continue
        if pid not in latest_vitals or v.get("date", "") > latest_vitals[pid].get("date", ""):
            latest_vitals[pid] = v

    if not latest_vitals:
        return False, "No vitals with SpO2 found."

    min_spo2 = None
    min_pid = None
    for pid, v in latest_vitals.items():
        spo2 = v.get("oxygenSaturation")
        if spo2 is not None and (min_spo2 is None or spo2 < min_spo2):
            min_spo2 = spo2
            min_pid = pid

    # Find patient
    patient = None
    for p in state.get("patients", []):
        if p.get("id") == min_pid:
            patient = p
            break
    if not patient:
        return False, f"Patient {min_pid} not found."
    last_name = patient.get("lastName", "?")

    # Find E* Problem-Focused Visit template
    pf_tmpl_id = None
    for t in state.get("visitNoteTemplates", []):
        if "problem-focused" in t.get("name", "").lower():
            pf_tmpl_id = t.get("id")
            break
    if not pf_tmpl_id:
        return False, "E* Problem-Focused Visit template not found."

    # Find a new signed note for this patient with that template
    # Existing notes for Bergstrom: note_011
    existing_note_ids = set()
    for n in state.get("visitNotes", []):
        if n.get("patientId") == min_pid:
            # Collect IDs of notes that existed in seed
            if n.get("id") in ("note_011",):
                existing_note_ids.add(n.get("id"))

    new_notes = [
        n for n in state.get("visitNotes", [])
        if n.get("patientId") == min_pid and n.get("id") not in existing_note_ids
    ]

    matching = None
    for n in new_notes:
        tmpl = n.get("templateUsed", "")
        if tmpl == pf_tmpl_id and n.get("status") == "signed":
            matching = n
            break

    if not matching:
        return False, (
            f"{last_name} (lowest SpO2={min_spo2}) does not have a new signed visit note "
            f"with E* Problem-Focused Visit template."
        )

    # Check blocks
    blocks = matching.get("blocks", [])
    block_types = [b.get("type", "").lower() for b in blocks]
    errors = []
    if "hpi" not in block_types:
        errors.append("New note missing HPI block.")
    if "assessment" not in block_types:
        errors.append("New note missing Assessment block.")

    if errors:
        return False, " ".join(errors)
    return True, (
        f"{last_name} (lowest SpO2={min_spo2}) has a new signed note (id={matching['id']}) "
        f"with E* Problem-Focused template, HPI and Assessment blocks."
    )
