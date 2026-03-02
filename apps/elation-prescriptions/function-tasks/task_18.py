import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    med_name = "Montelukast 10mg tablet"

    # Check that the med is NOT in permanentRxMeds anymore
    permanent_rx_meds = state.get("permanentRxMeds", [])
    perm_match = [m for m in permanent_rx_meds if m.get("medicationName") == med_name]
    if perm_match:
        return False, f"'{med_name}' is still in permanentRxMeds. Expected it to be discontinued."

    # Check that the med IS in discontinuedMeds
    discontinued_meds = state.get("discontinuedMeds", [])
    disc_match = [m for m in discontinued_meds if m.get("medicationName") == med_name]
    if not disc_match:
        return False, f"'{med_name}' not found in discontinuedMeds."

    med = disc_match[0]

    # Check discontinue reason
    reason = med.get("discontinueReason")
    expected_reason = "Patient stopped taking medication"
    if reason != expected_reason:
        return False, f"'{med_name}' discontinueReason is '{reason}', expected '{expected_reason}'."

    return True, f"'{med_name}' successfully discontinued with reason '{expected_reason}'."
