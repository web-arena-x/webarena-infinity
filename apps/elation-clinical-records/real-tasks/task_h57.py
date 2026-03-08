import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Create 'Mental Health Visit' category with MIPS, create note for Nakamura with that category + Telehealth template, add HPI + Psychological Status blocks, billing 99214, sign."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Check Mental Health Visit category exists with MIPS
    mh_cat = None
    for c in state.get("visitNoteCategories", []):
        if c.get("name", "").lower() == "mental health visit":
            mh_cat = c
            break
    if not mh_cat:
        return False, "Category 'Mental Health Visit' not found."
    if not mh_cat.get("countForMIPS"):
        errors.append("'Mental Health Visit' category does not have MIPS tracking enabled.")

    # Find Nakamura
    nakamura = None
    for p in state.get("patients", []):
        if p.get("lastName") == "Nakamura":
            nakamura = p
            break
    if not nakamura:
        return False, "Patient Nakamura not found."

    # Find Telehealth Follow-Up template
    tele_tmpl_id = None
    for t in state.get("visitNoteTemplates", []):
        if "telehealth" in t.get("name", "").lower() and "follow" in t.get("name", "").lower():
            tele_tmpl_id = t.get("id")
            break
    if not tele_tmpl_id:
        return False, "Telehealth Follow-Up template not found."

    # Find new note for Nakamura
    existing_note_ids = {"note_004"}
    new_notes = [
        n for n in state.get("visitNotes", [])
        if n.get("patientId") == nakamura["id"] and n.get("id") not in existing_note_ids
    ]

    matching = None
    for n in new_notes:
        cat = n.get("category") or n.get("categoryId", "")
        tmpl = n.get("templateUsed", "")
        if mh_cat and cat == mh_cat.get("id") and tmpl == tele_tmpl_id:
            matching = n
            break

    if not matching:
        errors.append(
            "Nakamura does not have a new note with 'Mental Health Visit' category "
            "and Telehealth Follow-Up template."
        )
    else:
        # Check blocks
        blocks = matching.get("blocks", [])
        block_types = [b.get("type", "").lower() for b in blocks]
        if "hpi" not in block_types:
            errors.append("Note missing HPI block.")
        if "psychological_status" not in block_types:
            errors.append("Note missing Psychological Status block.")

        # Check billing
        billing = matching.get("billingItems", [])
        has_99214 = any(b.get("cptCode") == "99214" for b in billing)
        if not has_99214:
            errors.append("Note missing billing code 99214.")

        # Check signed
        if matching.get("status") != "signed":
            errors.append(f"Note status is '{matching.get('status')}', expected 'signed'.")

    if errors:
        return False, " ".join(errors)
    return True, (
        f"'Mental Health Visit' category with MIPS created. Nakamura has signed note "
        f"(id={matching['id']}) with that category, Telehealth template, "
        f"HPI + Psychological Status blocks, and billing 99214."
    )
