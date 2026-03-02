import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    practice_areas = state.get("practiceAreas", [])
    personal_injury = next(
        (pa for pa in practice_areas if pa.get("name") == "Personal Injury"),
        None
    )

    if personal_injury is None:
        return False, "Could not find a practice area named 'Personal Injury'."

    stages = personal_injury.get("stages", [])
    stage_1_1 = next(
        (s for s in stages if s.get("id") == "stage_1_1"),
        None
    )

    if stage_1_1 is None:
        return False, "Could not find stage with id 'stage_1_1' under Personal Injury."

    if stage_1_1.get("name") != "Case Intake":
        return False, (
            f"Stage stage_1_1 under Personal Injury is named "
            f"'{stage_1_1.get('name')}', expected 'Case Intake'."
        )

    return True, "Personal Injury stage 'stage_1_1' has been renamed to 'Case Intake'."
