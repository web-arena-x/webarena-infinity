import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Find Rodriguez-Martinez (pat_004)
    patients = state.get("patients", [])
    rodriguez = None
    for p in patients:
        if p.get("lastName") == "Rodriguez-Martinez":
            rodriguez = p
            break
    if not rodriguez:
        return False, "Patient with lastName 'Rodriguez-Martinez' not found."

    patient_id = rodriguez.get("id", "pat_004")

    # Check for a problem with title containing "Acute Bronchitis" and icd10 "J20.9"
    problems = state.get("problems", [])
    rod_problems = [pr for pr in problems if pr.get("patientId") == patient_id]

    bronchitis_found = False
    for pr in rod_problems:
        title = (pr.get("title") or "").lower()
        icd10 = pr.get("icd10", "")
        if "acute bronchitis" in title and icd10 == "J20.9":
            bronchitis_found = True
            break

    if not bronchitis_found:
        problem_details = [
            f"id={pr.get('id')}: title={pr.get('title')}, icd10={pr.get('icd10')}"
            for pr in rod_problems
        ]
        return False, (
            f"No problem for Rodriguez-Martinez with title containing 'Acute Bronchitis' "
            f"and icd10='J20.9'. Current problems: {'; '.join(problem_details) if problem_details else 'none'}"
        )

    # Check for a new visit note (not note_009) with templateUsed tmpl_002 and status signed
    existing_note_ids = {"note_009"}
    notes = state.get("visitNotes", [])
    rod_new_notes = [
        n for n in notes
        if n.get("patientId") == patient_id and n.get("id") not in existing_note_ids
    ]

    if not rod_new_notes:
        return False, (
            "No new visit note found for Rodriguez-Martinez "
            "(existing note note_009 excluded)."
        )

    for note in rod_new_notes:
        template = note.get("templateUsed")
        status = note.get("status", "")
        if template == "tmpl_002" and status == "signed":
            return True, (
                f"Rodriguez-Martinez has Acute Bronchitis (J20.9) problem and a new "
                f"signed note (id={note.get('id')}) with templateUsed=tmpl_002."
            )

    # Diagnostics
    details = []
    for note in rod_new_notes:
        details.append(
            f"id={note.get('id')}: templateUsed={note.get('templateUsed')}, "
            f"status={note.get('status')}"
        )
    return False, (
        f"Rodriguez-Martinez has the Acute Bronchitis problem but no new note with "
        f"templateUsed=tmpl_002 and status='signed'. "
        f"Found {len(rod_new_notes)} new note(s): {'; '.join(details)}"
    )
