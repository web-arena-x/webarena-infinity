import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Find Personal Injury practice area
    practice_areas = state.get("practiceAreas", [])
    pi_pa = next(
        (pa for pa in practice_areas if pa.get("id") == "pa_1" or "personal injury" in pa.get("name", "").lower()),
        None
    )

    if pi_pa is None:
        return False, "Could not find Personal Injury practice area."

    pi_pa_id = pi_pa["id"]

    # Find all open PI matters
    matters = state.get("matters", [])
    open_pi_matters = [
        m for m in matters
        if m.get("practiceAreaId") == pi_pa_id and m.get("status") == "open"
    ]

    # Check that none of the open PI matters have responsibleAttorneyId == "user_8" (Robert Jackson)
    still_robert = [
        m for m in open_pi_matters
        if m.get("responsibleAttorneyId") == "user_8"
    ]

    if still_robert:
        names = [f"{m.get('id')} ('{m.get('description', '')}')" for m in still_robert]
        errors.append(
            f"{len(still_robert)} open PI matter(s) still assigned to Robert Jackson (user_8): {', '.join(names)}."
        )

    # Check that Marcus Williams (user_2) now has open PI matters
    marcus_matters = [
        m for m in open_pi_matters
        if m.get("responsibleAttorneyId") == "user_2"
    ]

    # Robert Jackson originally had these open PI matters:
    # matter_4, matter_6, matter_7, matter_8, matter_20, matter_24, matter_27
    expected_reassigned_ids = {"matter_4", "matter_6", "matter_7", "matter_8", "matter_20", "matter_24", "matter_27"}
    marcus_matter_ids = {m.get("id") for m in marcus_matters}

    reassigned = expected_reassigned_ids & marcus_matter_ids
    if len(reassigned) < 5:
        missing = expected_reassigned_ids - marcus_matter_ids
        errors.append(
            f"Only {len(reassigned)} of the 7 expected matters were reassigned to Marcus Williams (user_2). "
            f"Missing: {missing}."
        )

    if errors:
        return False, "Robert Jackson's open PI matters not fully reassigned to Marcus Williams. " + " | ".join(errors)

    return True, "All of Robert Jackson's open PI matters have been reassigned to Marcus Williams."
