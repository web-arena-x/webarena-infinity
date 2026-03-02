import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    med_name = "Ciprofloxacin 500mg tablet"

    # Check that the med is NOT in temporaryMeds anymore
    temporary_meds = state.get("temporaryMeds", [])
    temp_match = [m for m in temporary_meds if m.get("medicationName") == med_name]
    if temp_match:
        return False, f"'{med_name}' is still in temporaryMeds. Expected it to be discontinued."

    # Check that the med IS in discontinuedMeds
    discontinued_meds = state.get("discontinuedMeds", [])
    disc_match = [m for m in discontinued_meds if m.get("medicationName") == med_name]
    if not disc_match:
        return False, f"'{med_name}' not found in discontinuedMeds. Expected it to appear there after discontinuation."

    return True, f"'{med_name}' successfully removed from temporaryMeds and found in discontinuedMeds."
