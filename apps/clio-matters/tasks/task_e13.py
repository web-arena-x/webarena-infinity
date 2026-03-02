import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    matters = state.get("matters", [])
    mills_active = next(
        (m for m in matters
         if "Mills" in m.get("description", "") and
         "motorcycle" in m.get("description", "").lower()),
        None
    )

    if mills_active is not None:
        return False, "A matter containing 'Mills' and 'Motorcycle' still exists in active matters."

    deleted_matters = state.get("deletedMatters", [])
    mills_deleted = next(
        (m for m in deleted_matters
         if "Mills" in m.get("description", "") and
         "motorcycle" in m.get("description", "").lower()),
        None
    )

    if mills_deleted is None:
        return False, "No deleted matter found containing 'Mills' and 'Motorcycle' in deletedMatters."

    return True, "Mills motorcycle collision matter has been deleted and appears in deletedMatters."
