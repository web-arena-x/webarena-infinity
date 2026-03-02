import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    templates = state.get("matterTemplates", [])

    # Check 1: No template with name "Personal Injury - Slip and Fall" exists
    slip_and_fall = [
        t for t in templates
        if t.get("name", "").lower() == "personal injury - slip and fall"
    ]
    if slip_and_fall:
        errors.append(
            f"Template 'Personal Injury - Slip and Fall' still exists (id: {slip_and_fall[0].get('id')})."
        )

    # Find Personal Injury practice area
    practice_areas = state.get("practiceAreas", [])
    pi_pa = next(
        (pa for pa in practice_areas if pa.get("id") == "pa_1" or "personal injury" in pa.get("name", "").lower()),
        None
    )
    pi_pa_id = pi_pa["id"] if pi_pa else "pa_1"

    # Check 2: A template with "Premises Liability" exists with contingency billing and PI practice area
    premises_template = next(
        (t for t in templates if "premises liability" in t.get("name", "").lower()),
        None
    )
    if premises_template is None:
        template_names = [t.get("name") for t in templates]
        errors.append(
            f"No template containing 'Premises Liability' found. "
            f"Existing templates: {template_names}."
        )
    else:
        if premises_template.get("billingMethod") != "contingency":
            errors.append(
                f"Premises Liability template has billingMethod '{premises_template.get('billingMethod')}', "
                f"expected 'contingency'."
            )
        if premises_template.get("practiceAreaId") != pi_pa_id:
            errors.append(
                f"Premises Liability template has practiceAreaId '{premises_template.get('practiceAreaId')}', "
                f"expected '{pi_pa_id}' (Personal Injury)."
            )

    if errors:
        return False, "Template changes not correct. " + " | ".join(errors)

    return True, "Slip and Fall template deleted and Premises Liability template created with contingency billing under Personal Injury."
