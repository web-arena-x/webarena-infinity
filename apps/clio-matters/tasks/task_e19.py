import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    matters = state.get("matters", [])
    deluca = next(
        (m for m in matters
         if "DeLuca" in m.get("description", "") and
         ("felony" in m.get("description", "").lower() and
          "dui" in m.get("description", "").lower())),
        None
    )

    if deluca is None:
        # Fallback: try just "DeLuca"
        deluca = next(
            (m for m in matters
             if "DeLuca" in m.get("description", "")),
            None
        )
        if deluca is None:
            return False, "Could not find a matter with description containing 'DeLuca'."

    attorney_id = deluca.get("responsibleAttorneyId")

    if attorney_id is None:
        return False, "DeLuca matter has no responsibleAttorneyId set."

    if attorney_id != "user_8":
        return False, (
            f"DeLuca matter responsibleAttorneyId is '{attorney_id}', "
            f"expected 'user_8' (Robert Jackson)."
        )

    return True, "DeLuca matter has been reassigned to Robert Jackson (user_8)."
