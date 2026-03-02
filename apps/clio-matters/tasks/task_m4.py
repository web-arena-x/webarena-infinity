import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Find the Immigration practice area
    practice_areas = state.get("practiceAreas", [])
    immigration_pa = next(
        (pa for pa in practice_areas if pa.get("name", "").lower() == "immigration"),
        None
    )

    immigration_pa_id = "pa_8"
    if immigration_pa is not None:
        immigration_pa_id = immigration_pa.get("id", "pa_8")

    templates = state.get("matterTemplates", [])
    matching = next(
        (t for t in templates
         if "immigration" in t.get("name", "").lower()),
        None
    )

    if matching is None:
        template_names = [t.get("name", "") for t in templates]
        return False, f"No template with name containing 'Immigration' found. Existing templates: {template_names}."

    errors = []

    if matching.get("practiceAreaId") != immigration_pa_id:
        errors.append(
            f"Template practice area is '{matching.get('practiceAreaId')}', expected '{immigration_pa_id}' (Immigration)."
        )

    if matching.get("billingMethod") != "hourly":
        errors.append(
            f"Template billing method is '{matching.get('billingMethod')}', expected 'hourly'."
        )

    if errors:
        return False, " ".join(errors)

    return True, "Immigration template exists with correct practice area and hourly billing method."
