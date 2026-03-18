import requests


def verify(server_url: str) -> tuple[bool, str]:
    """William Thornton: approve urgent refill, modify-approve routine refill."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    if state.get("currentPatientId") != "pat_004":
        errors.append(f"Expected currentPatientId 'pat_004' (William Thornton), got '{state.get('currentPatientId')}'.")

    # rr_010 (Furosemide, urgent) -> approved
    rr_010 = next((r for r in state["refillRequests"] if r["id"] == "rr_010"), None)
    if not rr_010:
        errors.append("Refill request rr_010 not found.")
    else:
        if rr_010.get("status") != "approved":
            errors.append(f"Expected rr_010 (Furosemide, urgent) status 'approved', got '{rr_010.get('status')}'.")

    # rr_007 (Valsartan, routine) -> modified
    rr_007 = next((r for r in state["refillRequests"] if r["id"] == "rr_007"), None)
    if not rr_007:
        errors.append("Refill request rr_007 not found.")
    else:
        if rr_007.get("status") != "modified":
            errors.append(f"Expected rr_007 (Valsartan, routine) status 'modified', got '{rr_007.get('status')}'.")
        if rr_007.get("modifiedDetails") and "320mg" not in rr_007.get("modifiedDetails", ""):
            errors.append(f"Expected rr_007 modifiedDetails to mention '320mg', got '{rr_007.get('modifiedDetails')}'.")

    if errors:
        return False, " ".join(errors)
    return True, "William's urgent refill approved and routine refill modified with dose increase note."
