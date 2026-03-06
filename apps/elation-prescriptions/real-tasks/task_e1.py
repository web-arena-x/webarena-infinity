import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Find the Gabapentin refill request
    refill_requests = state.get("refillRequests", [])
    gabapentin_refill = None
    for req in refill_requests:
        if req.get("medicationName") == "Gabapentin 300mg capsule":
            gabapentin_refill = req
            break

    if gabapentin_refill is None:
        return False, "Gabapentin 300mg capsule refill request not found in refillRequests"

    if gabapentin_refill.get("status") != "approved":
        return False, f"Gabapentin refill status is '{gabapentin_refill.get('status')}', expected 'approved'"

    if not gabapentin_refill.get("processedBy"):
        return False, "Gabapentin refill processedBy is not set"

    if not gabapentin_refill.get("processedDate"):
        return False, "Gabapentin refill processedDate is not set"

    # Check that the permanent Rx med has an updated lastPrescribedDate
    permanent_rx_meds = state.get("permanentRxMeds", [])
    gabapentin_med = None
    for med in permanent_rx_meds:
        if med.get("medicationName") == "Gabapentin 300mg capsule":
            gabapentin_med = med
            break

    if gabapentin_med is None:
        return False, "Gabapentin 300mg capsule not found in permanentRxMeds"

    if gabapentin_med.get("lastPrescribedDate") == "2025-09-15":
        return False, "Gabapentin lastPrescribedDate is still the old value '2025-09-15'; expected it to be updated"

    return True, "Gabapentin refill request approved successfully with updated prescription date"
