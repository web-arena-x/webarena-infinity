import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Find patient with most vaccinations → create note with Vaccination Only category + COVID-19 Vaccine Visit template."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Count vaccination records per patient
    vax_counts = {}
    for v in state.get("vaccinations", []):
        pid = v.get("patientId")
        vax_counts[pid] = vax_counts.get(pid, 0) + 1

    if not vax_counts:
        return False, "No vaccination records found."

    max_pid = max(vax_counts, key=vax_counts.get)
    max_count = vax_counts[max_pid]

    # Find patient
    patient = None
    for p in state.get("patients", []):
        if p.get("id") == max_pid:
            patient = p
            break
    if not patient:
        return False, f"Patient {max_pid} not found."
    last_name = patient.get("lastName", "?")

    # Find Vaccination Only category
    vax_cat_id = None
    for c in state.get("visitNoteCategories", []):
        if c.get("name", "").lower() == "vaccination only":
            vax_cat_id = c.get("id")
            break
    if not vax_cat_id:
        return False, "Vaccination Only category not found."

    # Find COVID-19 Vaccine Visit template
    covid_tmpl_id = None
    for t in state.get("visitNoteTemplates", []):
        if "covid" in t.get("name", "").lower() and "vaccine" in t.get("name", "").lower():
            covid_tmpl_id = t.get("id")
            break
    if not covid_tmpl_id:
        return False, "COVID-19 Vaccine Visit template not found."

    # Find new note
    # Henderson's existing notes: note_001, note_002, note_003, note_hist_001
    existing_note_ids = {"note_001", "note_002", "note_003", "note_hist_001"}
    new_notes = [
        n for n in state.get("visitNotes", [])
        if n.get("patientId") == max_pid and n.get("id") not in existing_note_ids
    ]

    matching = None
    for n in new_notes:
        cat = n.get("category") or n.get("categoryId", "")
        tmpl = n.get("templateUsed", "")
        if cat == vax_cat_id and tmpl == covid_tmpl_id:
            matching = n
            break

    if not matching:
        return False, (
            f"{last_name} (most vaccinations: {max_count}) does not have a new visit note "
            f"with Vaccination Only category and COVID-19 Vaccine Visit template."
        )

    return True, (
        f"{last_name} (most vaccinations: {max_count}) has new note (id={matching['id']}) "
        f"with Vaccination Only category and COVID-19 Vaccine Visit template."
    )
