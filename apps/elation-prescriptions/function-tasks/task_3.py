import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that Gabapentin 300mg capsule refill was approved with modified sig."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Check refillRequests for Gabapentin 300mg capsule
    refill_requests = state.get("refillRequests", [])
    gabapentin_refill = None
    for rr in refill_requests:
        if rr.get("medicationName") == "Gabapentin 300mg capsule":
            gabapentin_refill = rr
            break

    if gabapentin_refill is None:
        return False, "No refill request found with medicationName='Gabapentin 300mg capsule'"

    # Check status is approved
    status = gabapentin_refill.get("status")
    if status != "approved":
        return False, f"Refill request status is '{status}', expected 'approved'"

    # Check linked medication in permanentRxMeds has updated sig
    permanent_rx_meds = state.get("permanentRxMeds", [])
    gabapentin_med = None
    for med in permanent_rx_meds:
        if med.get("medicationName") == "Gabapentin 300mg capsule":
            gabapentin_med = med
            break

    if gabapentin_med is None:
        return False, "No medication found with medicationName='Gabapentin 300mg capsule' in permanentRxMeds"

    expected_sig = "Take 1 capsule by mouth twice daily"
    actual_sig = gabapentin_med.get("sig", "")
    if actual_sig != expected_sig:
        return False, f"Gabapentin sig is '{actual_sig}', expected '{expected_sig}'"

    return True, (
        f"Gabapentin 300mg capsule refill approved with modified sig='{actual_sig}'"
    )
