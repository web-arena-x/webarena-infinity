import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    practice_areas = state.get("practiceAreas", [])
    criminal_defense = next(
        (pa for pa in practice_areas
         if "criminal" in pa.get("name", "").lower() and "defense" in pa.get("name", "").lower()),
        None
    )

    if criminal_defense is None:
        return False, "Could not find a practice area named 'Criminal Defense'."

    stages = criminal_defense.get("stages", [])
    stage_names = [s.get("name", "") for s in stages]
    stage_names_lower = [n.lower() for n in stage_names]

    # Check that Plea Negotiation is gone
    if any("plea negotiation" in n for n in stage_names_lower):
        return False, f"Criminal Defense still has a 'Plea Negotiation' stage. Current stages: {stage_names}."

    # Check that Pre-Trial/Plea exists
    if not any("pre-trial/plea" in n.lower() for n in stage_names):
        return False, f"Criminal Defense does not have a stage named 'Pre-Trial/Plea'. Current stages: {stage_names}."

    return True, "Criminal Defense has no 'Plea Negotiation' stage and has a 'Pre-Trial/Plea' stage."
