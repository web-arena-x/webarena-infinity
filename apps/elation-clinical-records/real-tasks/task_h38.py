import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    appointment_types = state.get("appointmentTypes", [])

    # Find Procedure appointment type (apt_007)
    procedure = None
    for apt in appointment_types:
        name = (apt.get("name") or "").strip()
        if name.lower() == "procedure" or apt.get("id") == "apt_007":
            procedure = apt
            break

    if not procedure:
        apt_names = [a.get("name") for a in appointment_types]
        return False, (
            f"Appointment type 'Procedure' not found. "
            f"Available types: {apt_names}"
        )

    errors = []

    # Check noteTemplate = tmpl_002 (from Office Visit)
    template = procedure.get("noteTemplate")
    if template != "tmpl_002":
        errors.append(
            f"Procedure noteTemplate is '{template}', expected 'tmpl_002' "
            f"(E&M Problem-Focused Visit from Office Visit)."
        )

    # Check noteCategory = cat_005 (from Follow-Up)
    category = procedure.get("noteCategory")
    if category != "cat_005":
        errors.append(
            f"Procedure noteCategory is '{category}', expected 'cat_005' "
            f"(Follow-Up category)."
        )

    # Check noteFormat = hp_single
    fmt = procedure.get("noteFormat")
    if fmt != "hp_single":
        errors.append(
            f"Procedure noteFormat is '{fmt}', expected 'hp_single'."
        )

    if errors:
        return False, " ".join(errors)

    return True, (
        "Procedure appointment type has noteTemplate=tmpl_002, "
        "noteCategory=cat_005, and noteFormat=hp_single."
    )
