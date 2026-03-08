import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Find template with POS '02', duplicate it, rename to 'Virtual Care Standard', assign to Telehealth Visit."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Check that 'Virtual Care Standard' template exists
    vcs_tmpl = None
    for t in state.get("visitNoteTemplates", []):
        if t.get("name", "").lower() == "virtual care standard":
            vcs_tmpl = t
            break

    if not vcs_tmpl:
        return False, "Template 'Virtual Care Standard' not found."

    # Verify it's a copy of the POS '02' template (tmpl_003 Telehealth Follow-Up)
    # Should have the same content structure
    original = None
    for t in state.get("visitNoteTemplates", []):
        if t.get("id") == "tmpl_003":
            original = t
            break

    if original:
        orig_content = original.get("content", {})
        copy_content = vcs_tmpl.get("content", {})
        for key in orig_content:
            if orig_content.get(key) and not copy_content.get(key):
                errors.append(
                    f"Template 'Virtual Care Standard' missing content section '{key}' "
                    f"from the original."
                )

    # Check Telehealth Visit appointment type uses this template
    tele_apt = None
    for a in state.get("appointmentTypes", []):
        if a.get("name", "").lower() == "telehealth visit":
            tele_apt = a
            break
    if not tele_apt:
        errors.append("Telehealth Visit appointment type not found.")
    elif tele_apt.get("noteTemplate") != vcs_tmpl.get("id"):
        errors.append(
            f"Telehealth Visit template is '{tele_apt.get('noteTemplate')}', "
            f"expected '{vcs_tmpl.get('id')}' (Virtual Care Standard)."
        )

    if errors:
        return False, " ".join(errors)
    return True, (
        f"Template 'Virtual Care Standard' (id={vcs_tmpl['id']}) created as duplicate of POS '02' template. "
        f"Telehealth Visit appointment now uses it."
    )
