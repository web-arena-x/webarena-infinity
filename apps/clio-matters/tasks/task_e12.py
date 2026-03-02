import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    practice_areas = state.get("practiceAreas", [])
    real_estate = next(
        (pa for pa in practice_areas if pa.get("name") == "Real Estate"),
        None
    )

    if real_estate is None:
        return False, "Could not find a practice area named 'Real Estate'."

    stages = real_estate.get("stages", [])
    closing_stage = next(
        (s for s in stages if s.get("name") == "Closing"),
        None
    )

    if closing_stage is not None:
        return False, "The 'Closing' stage still exists under Real Estate."

    return True, "The 'Closing' stage has been deleted from Real Estate."
