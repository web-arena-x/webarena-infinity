import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    med_name = "Omeprazole 20mg capsule"

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

    # Check status
    status = med.get("status")
    if status != "discontinued":
        return False, f"'{med_name}' in discontinuedMeds has status '{status}', expected 'discontinued'."

    # Check discontinue reason
    reason = med.get("discontinueReason")
    expected_reason = "I want to discontinue this medication"
    if reason != expected_reason:
        return False, f"'{med_name}' discontinueReason is '{reason}', expected '{expected_reason}'."

    return True, f"'{med_name}' successfully discontinued with correct reason '{expected_reason}'."
