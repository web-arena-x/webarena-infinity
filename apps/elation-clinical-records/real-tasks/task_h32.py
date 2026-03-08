import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify 'COPD Management' template with HPI + billing 99214, and a new note for Bergstrom using it."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    errors = []

    # Check 1: Template named "COPD Management" exists
    templates = state.get("visitNoteTemplates", [])
    copd_template = None
    for t in templates:
        if t.get("name", "").lower() == "copd management":
            copd_template = t
            break

    if copd_template is None:
        errors.append("No template named 'COPD Management' found")
        return False, "; ".join(errors)

    template_id = copd_template.get("id", "")

    # Check 1a: content.hpi is non-empty
    content = copd_template.get("content", {})
    hpi = content.get("hpi", "")
    if not hpi:
        errors.append("Template 'COPD Management' has empty or missing content.hpi")

    # Check 1b: billing item with cptCode "99214"
    billing = copd_template.get("billingItems", [])
    has_99214 = any(b.get("cptCode") == "99214" for b in billing)
    if not has_99214:
        errors.append("Template 'COPD Management' does not have a billing item with cptCode '99214'")

    # Check 2: A new visit note for Bergstrom (pat_007) that is not note_011
    visit_notes = state.get("visitNotes", [])
    bergstrom_new_notes = [
        n for n in visit_notes
        if n.get("patientId") == "pat_007" and n.get("id") != "note_011"
    ]

    if not bergstrom_new_notes:
        errors.append("No new visit note found for Bergstrom (pat_007) besides note_011")
    else:
        new_note = bergstrom_new_notes[0]
        used_template = new_note.get("templateUsed", "")
        if used_template != template_id:
            errors.append(
                f"New Bergstrom note has templateUsed '{used_template}', expected '{template_id}'"
            )

    if errors:
        return False, "; ".join(errors)
    return True, "COPD Management template exists with HPI + 99214 billing, and Bergstrom has a new note using it"
