import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify default format changed to hp_single, new Follow-Up note for Nakamura with HPI block, signed."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    errors = []

    # Check 1: providerPreferences.defaultNoteFormat == "hp_single"
    prefs = state.get("providerPreferences", {})
    default_format = prefs.get("defaultNoteFormat", "")
    if default_format != "hp_single":
        errors.append(
            f"providerPreferences.defaultNoteFormat is '{default_format}', expected 'hp_single'"
        )

    # Check 2: A new visit note for Nakamura (pat_002) that is not note_004
    visit_notes = state.get("visitNotes", [])
    nakamura_notes = [
        n for n in visit_notes
        if n.get("patientId") == "pat_002" and n.get("id") != "note_004"
    ]
    if not nakamura_notes:
        errors.append("No new visit note found for Nakamura (pat_002) besides note_004")
        if errors:
            return False, "; ".join(errors)

    new_note = nakamura_notes[0]

    # Check 2b: category is cat_005 (Follow-Up)
    category = new_note.get("category", "")
    if category != "cat_005":
        errors.append(
            f"New Nakamura note has category '{category}', expected 'cat_005' (Follow-Up)"
        )

    # Check 3: Note has a block with type "hpi"
    blocks = new_note.get("blocks", [])
    has_hpi = any(b.get("type", "").lower() == "hpi" for b in blocks)
    if not has_hpi:
        errors.append("New Nakamura note does not have a block with type 'hpi'")

    # Check 4: Note has status "signed"
    status = new_note.get("status", "")
    if status != "signed":
        errors.append(
            f"New Nakamura note has status '{status}', expected 'signed'"
        )

    if errors:
        return False, "; ".join(errors)
    return True, "Default format is hp_single, new signed Follow-Up note for Nakamura with HPI block exists"
