import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Check 1: Appellate Practice practice area exists with at least 3 stages
    practice_areas = state.get("practiceAreas", [])
    appellate_pa = next(
        (pa for pa in practice_areas if "appellate practice" in pa.get("name", "").lower()),
        None
    )

    if appellate_pa is None:
        pa_names = [pa.get("name") for pa in practice_areas]
        errors.append(
            f"No practice area named 'Appellate Practice' found. "
            f"Existing practice areas: {pa_names}."
        )
    else:
        stages = appellate_pa.get("stages", [])
        if len(stages) < 3:
            errors.append(
                f"Appellate Practice has {len(stages)} stage(s), expected at least 3."
            )

        stage_names_lower = [s.get("name", "").lower() for s in stages]
        required_stages = {
            "notice of appeal": "Notice of Appeal",
            "brief writing": "Brief Writing",
            "oral argument": "Oral Argument"
        }
        missing = []
        for key, display in required_stages.items():
            if key not in stage_names_lower:
                missing.append(display)

        if missing:
            actual_names = [s.get("name", "") for s in stages]
            errors.append(
                f"Appellate Practice is missing stage(s): {missing}. "
                f"Found stages: {actual_names}."
            )

    # Check 2: Hernandez armed robbery matter has practiceAreaId matching Appellate Practice
    matters = state.get("matters", [])
    hernandez = None
    for m in matters:
        desc = m.get("description", "").lower()
        if "hernandez" in desc and ("armed robbery" in desc or "alibi" in desc):
            hernandez = m
            break

    if hernandez is None:
        errors.append(
            "Could not find Hernandez armed robbery matter "
            "(description containing 'Hernandez' and 'armed robbery' or 'alibi')."
        )
    elif appellate_pa is not None:
        if hernandez.get("practiceAreaId") != appellate_pa["id"]:
            errors.append(
                f"Hernandez matter has practiceAreaId '{hernandez.get('practiceAreaId')}', "
                f"expected '{appellate_pa['id']}' (Appellate Practice)."
            )
    else:
        # Appellate PA not found, so can't verify assignment
        errors.append(
            "Cannot verify Hernandez matter assignment because Appellate Practice PA was not found."
        )

    if errors:
        return False, "Appellate Practice setup not correct. " + " | ".join(errors)

    return True, "Appellate Practice practice area created with required stages and Hernandez armed robbery matter reassigned to it."
