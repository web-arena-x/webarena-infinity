import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    practice_areas = state.get("practiceAreas", [])
    criminal_defense = next(
        (pa for pa in practice_areas if pa.get("name") == "Criminal Defense"),
        None
    )

    if criminal_defense is None:
        return False, "Could not find a practice area named 'Criminal Defense'."

    stages = criminal_defense.get("stages", [])
    appeals_stage = next(
        (s for s in stages if s.get("name") == "Appeals"),
        None
    )

    if appeals_stage is None:
        return False, "No stage named 'Appeals' found under Criminal Defense."

    return True, "An 'Appeals' stage has been added to Criminal Defense."
