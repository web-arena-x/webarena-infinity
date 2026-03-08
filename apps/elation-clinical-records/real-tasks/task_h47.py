import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Disable MIPS on default category, create 'Quality Metrics' with MIPS, assign to Annual Exam."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Check that the original default category (Office Visit / cat_001) has MIPS disabled
    office_visit = None
    for c in state.get("visitNoteCategories", []):
        if c.get("id") == "cat_001" or c.get("name", "").lower() == "office visit":
            office_visit = c
            break
    if not office_visit:
        return False, "Office Visit category (cat_001) not found."
    if office_visit.get("countForMIPS") is not False:
        errors.append("Office Visit category still has MIPS enabled; expected disabled.")

    # Check Quality Metrics category exists with MIPS enabled
    quality_cat = None
    for c in state.get("visitNoteCategories", []):
        if c.get("name", "").lower() == "quality metrics":
            quality_cat = c
            break
    if not quality_cat:
        errors.append("Category 'Quality Metrics' not found.")
    elif not quality_cat.get("countForMIPS"):
        errors.append("'Quality Metrics' category does not have MIPS tracking enabled.")

    # Check Annual Exam appointment uses the Quality Metrics category
    annual_apt = None
    for a in state.get("appointmentTypes", []):
        if a.get("name", "").lower() == "annual exam":
            annual_apt = a
            break
    if not annual_apt:
        errors.append("Annual Exam appointment type not found.")
    elif quality_cat:
        if annual_apt.get("noteCategory") != quality_cat.get("id"):
            errors.append(
                f"Annual Exam appointment uses category '{annual_apt.get('noteCategory')}', "
                f"expected '{quality_cat.get('id')}' (Quality Metrics)."
            )

    if errors:
        return False, " ".join(errors)
    return True, (
        "Office Visit MIPS disabled, 'Quality Metrics' category created with MIPS, "
        "Annual Exam appointment type uses Quality Metrics."
    )
