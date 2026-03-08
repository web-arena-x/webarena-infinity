import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Find draft note → add Social History + Follow Up blocks, billing 99215, sign."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # The only draft note in seed data is note_012 (Kowalski)
    note = None
    for n in state.get("visitNotes", []):
        if n.get("id") == "note_012":
            note = n
            break
    if not note:
        return False, "Note note_012 not found."

    errors = []

    # Check signed
    if note.get("status") != "signed":
        errors.append(f"Note note_012 status is '{note.get('status')}', expected 'signed'.")

    # Check blocks
    blocks = note.get("blocks", [])
    block_types = [b.get("type", "").lower() for b in blocks]

    if "social_history" not in block_types:
        errors.append("Note is missing a Social History block.")
    if "follow_up" not in block_types:
        errors.append("Note is missing a Follow Up block.")

    # Check billing
    billing = note.get("billingItems", [])
    has_99215 = any(b.get("cptCode") == "99215" for b in billing)
    if not has_99215:
        errors.append("Note is missing billing code 99215.")

    if errors:
        return False, " ".join(errors)
    return True, "Note note_012 has Social History + Follow Up blocks, billing 99215, and is signed."
