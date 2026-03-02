import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    deleted_matters = state.get("deletedMatters", [])
    smith_deleted = next(
        (m for m in deleted_matters
         if "Smith Consultation" in m.get("description", "")),
        None
    )

    if smith_deleted is not None:
        return False, "An entry with 'Smith Consultation' still exists in deletedMatters."

    matters = state.get("matters", [])
    smith_active = next(
        (m for m in matters
         if "Smith Consultation" in m.get("description", "")),
        None
    )

    if smith_active is None:
        return False, "No matter with 'Smith Consultation' found in active matters."

    return True, "Smith Consultation has been recovered from the recovery bin and is now in active matters."
