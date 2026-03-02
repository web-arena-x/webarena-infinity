import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    matter = next(
        (m for m in state.get("matters", [])
         if "McCarthy" in m.get("description", "")
         and ("pedestrian" in m.get("description", "").lower() or "crosswalk" in m.get("description", "").lower())),
        None
    )

    if matter is None:
        return False, "Could not find a matter with description containing 'McCarthy' and 'pedestrian' or 'crosswalk'."

    errors = []

    if matter.get("responsibleAttorneyId") != "user_2":
        errors.append(
            f"Responsible attorney is '{matter.get('responsibleAttorneyId')}', expected 'user_2' (Marcus Williams)."
        )

    if matter.get("stageId") != "stage_1_4":
        errors.append(
            f"Stage is '{matter.get('stageId')}', expected 'stage_1_4' (Litigation)."
        )

    if errors:
        return False, " ".join(errors)

    return True, "McCarthy matter has Marcus Williams as responsible attorney and is in Litigation stage."
