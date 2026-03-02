import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    practice_areas = state.get("practiceAreas", [])
    civil_rights = next(
        (pa for pa in practice_areas if pa.get("name", "").lower() == "civil rights"),
        None
    )

    if civil_rights is None:
        return False, "No practice area named 'Civil Rights' found."

    stages = civil_rights.get("stages", [])
    if len(stages) < 3:
        return False, f"Civil Rights practice area has {len(stages)} stage(s), expected at least 3."

    stage_names_lower = [s.get("name", "").lower() for s in stages]
    required = {"investigation", "filing", "resolution"}
    missing = [name for name in required if name not in stage_names_lower]

    if missing:
        actual_names = [s.get("name", "") for s in stages]
        return False, f"Civil Rights practice area is missing stage(s): {missing}. Found stages: {actual_names}."

    return True, "Civil Rights practice area exists with Investigation, Filing, and Resolution stages."
