import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    matters = state.get("matters", [])

    # Find TechNova matter
    technova = None
    for m in matters:
        if "TechNova" in (m.get("description") or ""):
            technova = m
            break

    if not technova:
        return False, "TechNova matter not found."

    technova_responsible = technova.get("responsibleAttorneyId")
    technova_originating = technova.get("originatingAttorneyId")

    # Find Rodriguez matter
    rodriguez = None
    for m in matters:
        desc = m.get("description") or ""
        if "Rodriguez" in desc and "Premier Auto" in desc:
            rodriguez = m
            break

    if not rodriguez:
        return False, "Rodriguez auto accident matter not found."

    errors = []

    actual_responsible = rodriguez.get("responsibleAttorneyId")
    if actual_responsible != technova_responsible:
        return False, (
            f"Rodriguez responsible attorney is '{actual_responsible}', "
            f"expected '{technova_responsible}' (TechNova's responsible attorney)."
        )

    actual_originating = rodriguez.get("originatingAttorneyId")
    if actual_originating != technova_originating:
        return False, (
            f"Rodriguez originating attorney is '{actual_originating}', "
            f"expected '{technova_originating}' (TechNova's originating attorney)."
        )

    return True, "Rodriguez attorneys updated to match TechNova's responsible and originating attorneys."
