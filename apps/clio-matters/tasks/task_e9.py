import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    matter = next(
        (m for m in state.get("matters", [])
         if "Dimitriou" in m.get("description", "") and "dog bite" in m.get("description", "").lower()),
        None
    )

    if matter is None:
        # Fall back to just checking for Dimitriou + Lawson
        matter = next(
            (m for m in state.get("matters", [])
             if "Dimitriou" in m.get("description", "") and "Lawson" in m.get("description", "")),
            None
        )

    if matter is None:
        return False, "Could not find a matter with description containing 'Dimitriou'."

    if matter.get("stageId") != "stage_1_2":
        return False, f"Dimitriou matter stageId is '{matter.get('stageId')}', expected 'stage_1_2' (Investigation)."

    return True, "Dimitriou matter has been moved to the Investigation stage."
