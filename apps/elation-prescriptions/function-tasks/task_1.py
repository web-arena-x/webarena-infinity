import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that the pending refill request for Lisinopril 10mg tablet was approved."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Check refillRequests for Lisinopril 10mg tablet
    refill_requests = state.get("refillRequests", [])
    lisinopril_refill = None
    for rr in refill_requests:
        if rr.get("medicationName") == "Lisinopril 10mg tablet":
            lisinopril_refill = rr
            break

    if lisinopril_refill is None:
        return False, "No refill request found with medicationName='Lisinopril 10mg tablet'"

    # Check status is approved
    status = lisinopril_refill.get("status")
    if status != "approved":
        return False, f"Refill request status is '{status}', expected 'approved'"

    # Check processedBy is set
    processed_by = lisinopril_refill.get("processedBy")
    if not processed_by:
        return False, "Refill request processedBy is not set"

    # Check processedDate is set
    processed_date = lisinopril_refill.get("processedDate")
    if not processed_date:
        return False, "Refill request processedDate is not set"

    # Check linked medication in permanentRxMeds has updated lastPrescribedDate
    permanent_rx_meds = state.get("permanentRxMeds", [])
    lisinopril_med = None
    for med in permanent_rx_meds:
        if med.get("medicationName") == "Lisinopril 10mg tablet":
            lisinopril_med = med
            break

    if lisinopril_med is None:
        return False, "No medication found with medicationName='Lisinopril 10mg tablet' in permanentRxMeds"

    last_prescribed = lisinopril_med.get("lastPrescribedDate")
    if last_prescribed == "2025-12-15":
        return False, f"lastPrescribedDate is still the seed value '2025-12-15', expected it to be updated after approval"

    if not last_prescribed:
        return False, "lastPrescribedDate is not set on Lisinopril 10mg tablet in permanentRxMeds"

    return True, (
        f"Lisinopril 10mg tablet refill request approved successfully. "
        f"processedBy='{processed_by}', processedDate='{processed_date}', "
        f"lastPrescribedDate updated to '{last_prescribed}'"
    )
