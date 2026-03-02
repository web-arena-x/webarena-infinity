import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Check for Appellate Law practice area
    practice_areas = state.get("practiceAreas", [])
    appellate_pa = next(
        (pa for pa in practice_areas if "appellate" in pa.get("name", "").lower()),
        None
    )

    if appellate_pa is None:
        return False, (
            "No practice area containing 'Appellate' found. "
            f"Existing practice areas: {[pa.get('name') for pa in practice_areas]}."
        )

    appellate_pa_id = appellate_pa.get("id")
    stages = appellate_pa.get("stages", [])

    if len(stages) < 4:
        errors.append(
            f"Appellate Law practice area has {len(stages)} stage(s), expected at least 4."
        )

    # Check required stage names
    stage_names_lower = [s.get("name", "").lower() for s in stages]
    required_stages = {
        "notice of appeal": "Notice of Appeal",
        "briefing": "Briefing",
        "oral argument": "Oral Argument",
        "decision": "Decision",
    }

    for key, display_name in required_stages.items():
        if key not in stage_names_lower:
            errors.append(
                f"Appellate Law practice area is missing stage '{display_name}'. "
                f"Found stages: {[s.get('name') for s in stages]}."
            )

    # Check for a template matching Appellate with billingMethod == "hourly"
    templates = state.get("matterTemplates", [])
    appellate_template = next(
        (t for t in templates if "appellate" in t.get("name", "").lower()),
        None
    )

    if appellate_template is None:
        errors.append(
            f"No matter template containing 'Appellate' found. "
            f"Existing templates: {[t.get('name') for t in templates]}."
        )
    else:
        if appellate_template.get("billingMethod") != "hourly":
            errors.append(
                f"Appellate template '{appellate_template.get('name')}' has billingMethod "
                f"'{appellate_template.get('billingMethod')}', expected 'hourly'."
            )

        if appellate_template.get("practiceAreaId") != appellate_pa_id:
            errors.append(
                f"Appellate template '{appellate_template.get('name')}' has practiceAreaId "
                f"'{appellate_template.get('practiceAreaId')}', expected '{appellate_pa_id}' "
                f"(Appellate Law)."
            )

    if errors:
        return False, "Appellate Law setup incomplete. " + " | ".join(errors)

    return True, (
        f"Appellate Law practice area ('{appellate_pa.get('name')}') created with stages "
        f"{[s.get('name') for s in stages]} and a matching hourly template "
        f"'{appellate_template.get('name')}'."
    )
