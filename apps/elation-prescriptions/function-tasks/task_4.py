import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that the pending refill request for Omeprazole 20mg capsule was approved."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Check refillRequests for Omeprazole 20mg capsule
    refill_requests = state.get("refillRequests", [])
    omeprazole_refill = None
    for rr in refill_requests:
        if rr.get("medicationName") == "Omeprazole 20mg capsule":
            omeprazole_refill = rr
            break

    if omeprazole_refill is None:
        return False, "No refill request found with medicationName='Omeprazole 20mg capsule'"

    # Check status is approved
    status = omeprazole_refill.get("status")
    if status != "approved":
        return False, f"Refill request status is '{status}', expected 'approved'"

    # Check processedBy is set
    processed_by = omeprazole_refill.get("processedBy")
    if not processed_by:
        return False, "Refill request processedBy is not set"

    return True, (
        f"Omeprazole 20mg capsule refill request approved successfully. "
        f"processedBy='{processed_by}'"
    )
