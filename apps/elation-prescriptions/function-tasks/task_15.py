import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    med_name = "Prednisone 10mg tablet"

    # Check that the med is NOT in temporaryMeds anymore
    temporary_meds = state.get("temporaryMeds", [])
    temp_match = [m for m in temporary_meds if m.get("medicationName") == med_name]
    if temp_match:
        return False, f"'{med_name}' is still in temporaryMeds. Expected it to be moved to permanentRxMeds."

    # Check that the med IS in permanentRxMeds with classification 'permanent_rx'
    permanent_rx_meds = state.get("permanentRxMeds", [])
    perm_match = [m for m in permanent_rx_meds if m.get("medicationName") == med_name]
    if not perm_match:
        return False, f"'{med_name}' not found in permanentRxMeds. Expected it to appear there after reclassification."

    med = perm_match[0]
    classification = med.get("classification")
    if classification != "permanent_rx":
        return False, f"'{med_name}' found in permanentRxMeds but classification is '{classification}', expected 'permanent_rx'."

    return True, f"'{med_name}' successfully moved from temporaryMeds to permanentRxMeds with classification 'permanent_rx'."
