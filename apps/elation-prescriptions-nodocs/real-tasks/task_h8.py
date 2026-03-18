import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    refill_requests = state.get("refillRequests", [])
    errors = []

    # Check rr_001 (Atorvastatin) is approved
    rr_001 = None
    for rr in refill_requests:
        if rr.get("id") == "rr_001":
            rr_001 = rr
            break

    if rr_001 is None:
        errors.append("Refill request rr_001 (Atorvastatin) not found.")
    elif rr_001.get("status") != "approved":
        errors.append(f"Expected rr_001 (Atorvastatin) status 'approved', got '{rr_001.get('status')}'.")

    # Check rr_002 (Metformin) is denied with reason containing "lab"
    rr_002 = None
    for rr in refill_requests:
        if rr.get("id") == "rr_002":
            rr_002 = rr
            break

    if rr_002 is None:
        errors.append("Refill request rr_002 (Metformin) not found.")
    else:
        if rr_002.get("status") != "denied":
            errors.append(f"Expected rr_002 (Metformin) status 'denied', got '{rr_002.get('status')}'.")
        deny_reason = str(rr_002.get("denyReason", ""))
        if "lab" not in deny_reason.lower():
            errors.append(f"Expected rr_002 denyReason to contain 'lab', got '{deny_reason}'.")

    # Check rr_011 (Sertraline) is denied with reason containing "changed"
    rr_011 = None
    for rr in refill_requests:
        if rr.get("id") == "rr_011":
            rr_011 = rr
            break

    if rr_011 is None:
        errors.append("Refill request rr_011 (Sertraline) not found.")
    else:
        if rr_011.get("status") != "denied":
            errors.append(f"Expected rr_011 (Sertraline) status 'denied', got '{rr_011.get('status')}'.")
        deny_reason = str(rr_011.get("denyReason", ""))
        if "changed" not in deny_reason.lower():
            errors.append(f"Expected rr_011 denyReason to contain 'changed', got '{deny_reason}'.")

    if errors:
        return False, " ".join(errors)

    return True, "All Margaret's refill requests processed: Atorvastatin approved, Metformin and Sertraline denied."
