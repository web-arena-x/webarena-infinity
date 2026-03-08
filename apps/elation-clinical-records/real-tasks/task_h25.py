import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Find Kowalski's draft note (note_012)
    notes = state.get("visitNotes", [])
    kowalski_note = None
    for n in notes:
        if n.get("id") == "note_012":
            kowalski_note = n
            break

    if not kowalski_note:
        return False, "Visit note 'note_012' (Kowalski's draft) not found."

    # Verify it belongs to Kowalski
    patients = state.get("patients", [])
    kowalski = None
    for p in patients:
        if p.get("lastName") == "Kowalski":
            kowalski = p
            break

    if kowalski and kowalski_note.get("patientId") != kowalski.get("id"):
        return False, (
            f"note_012 patientId is '{kowalski_note.get('patientId')}' but Kowalski's id "
            f"is '{kowalski.get('id')}' — unexpected mismatch."
        )

    # Check billing items for cptCode 99215 (from Pre-Op Evaluation template tmpl_010)
    billing_items = kowalski_note.get("billingItems", [])
    for bi in billing_items:
        cpt = str(bi.get("cptCode", ""))
        if cpt == "99215":
            return True, (
                f"Kowalski's draft note (note_012) has billing item with cptCode 99215 "
                f"(from Pre-Op Evaluation template)."
            )

    cpt_codes = [bi.get("cptCode") for bi in billing_items]
    return False, (
        f"Kowalski's draft note (note_012) does not have a billing item with cptCode 99215. "
        f"Current billing cptCodes: {cpt_codes}"
    )
