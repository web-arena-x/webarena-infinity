import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Find the Sertraline refill request
    refill_requests = state.get("refillRequests", [])
    sertraline_refill = None
    for req in refill_requests:
        if req.get("medicationName") == "Sertraline 50mg tablet":
            sertraline_refill = req
            break

    if sertraline_refill is None:
        return False, "Sertraline 50mg tablet refill request not found in refillRequests"

    if sertraline_refill.get("status") != "approved":
        return False, f"Sertraline refill status is '{sertraline_refill.get('status')}', expected 'approved'"

    if not sertraline_refill.get("processedBy"):
        return False, "Sertraline refill processedBy is not set"

    if not sertraline_refill.get("processedDate"):
        return False, "Sertraline refill processedDate is not set"

    # Check that the permanent Rx med has an updated lastPrescribedDate
    permanent_rx_meds = state.get("permanentRxMeds", [])
    sertraline_med = None
    for med in permanent_rx_meds:
        if med.get("medicationName") == "Sertraline 50mg tablet":
            sertraline_med = med
            break

    if sertraline_med is None:
        return False, "Sertraline 50mg tablet not found in permanentRxMeds"

    if sertraline_med.get("lastPrescribedDate") == "2026-01-05":
        return False, "Sertraline lastPrescribedDate is still the old value '2026-01-05'; expected it to be updated"

    return True, "Sertraline refill request approved successfully with updated prescription date"
