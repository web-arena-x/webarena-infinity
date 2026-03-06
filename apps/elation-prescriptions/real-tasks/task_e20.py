import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Find the Metoprolol Succinate refill request
    refill_requests = state.get("refillRequests", [])
    metoprolol_refill = None
    for req in refill_requests:
        if req.get("medicationName") == "Metoprolol Succinate ER 50mg tablet":
            metoprolol_refill = req
            break

    if metoprolol_refill is None:
        return False, "Metoprolol Succinate ER 50mg tablet refill request not found in refillRequests"

    if metoprolol_refill.get("status") != "approved":
        return False, f"Metoprolol refill status is '{metoprolol_refill.get('status')}', expected 'approved'"

    if not metoprolol_refill.get("processedBy"):
        return False, "Metoprolol refill processedBy is not set"

    if not metoprolol_refill.get("processedDate"):
        return False, "Metoprolol refill processedDate is not set"

    # Check that the permanent Rx med has an updated lastPrescribedDate
    permanent_rx_meds = state.get("permanentRxMeds", [])
    metoprolol_med = None
    for med in permanent_rx_meds:
        if med.get("medicationName") == "Metoprolol Succinate ER 50mg tablet":
            metoprolol_med = med
            break

    if metoprolol_med is None:
        return False, "Metoprolol Succinate ER 50mg tablet not found in permanentRxMeds"

    if metoprolol_med.get("lastPrescribedDate") == "2025-11-20":
        return False, "Metoprolol lastPrescribedDate is still the old value '2025-11-20'; expected it to be updated"

    return True, "Metoprolol Succinate refill request approved successfully with updated prescription date"
