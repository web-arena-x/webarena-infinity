import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Default format → pre_op. New 'Pre-Surgical Screening' category with MIPS.
    Procedure appointment → new category + Pre-Operative Evaluation template."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Check default format
    prefs = state.get("providerPreferences", {})
    if prefs.get("defaultNoteFormat") != "pre_op":
        errors.append(
            f"Default format should be 'pre_op', got '{prefs.get('defaultNoteFormat')}'."
        )

    # Check new category
    new_cat = None
    for c in state.get("visitNoteCategories", []):
        if c.get("name", "").lower() == "pre-surgical screening":
            new_cat = c
            break
    if not new_cat:
        errors.append("Category 'Pre-Surgical Screening' not found.")
    elif not new_cat.get("countForMIPS"):
        errors.append("'Pre-Surgical Screening' should have MIPS enabled.")

    # Check Procedure appointment
    procedure = None
    for apt in state.get("appointmentTypes", []):
        if apt.get("name") == "Procedure":
            procedure = apt
            break
    if not procedure:
        errors.append("Procedure appointment type not found.")
    else:
        # Should use new category
        if new_cat and procedure.get("noteCategory") != new_cat["id"]:
            errors.append(
                f"Procedure category should be '{new_cat['id']}', "
                f"got '{procedure.get('noteCategory')}'."
            )
        # Should use Pre-Operative Evaluation template
        preop_tmpl = None
        for t in state.get("visitNoteTemplates", []):
            if "pre-operative" in t.get("name", "").lower():
                preop_tmpl = t
                break
        if preop_tmpl and procedure.get("noteTemplate") != preop_tmpl["id"]:
            errors.append(
                f"Procedure template should be '{preop_tmpl['id']}', "
                f"got '{procedure.get('noteTemplate')}'."
            )

    if errors:
        return False, " ".join(errors)
    return True, (
        "Default format set to Pre-Op H&P. 'Pre-Surgical Screening' category created. "
        "Procedure appointment configured."
    )
