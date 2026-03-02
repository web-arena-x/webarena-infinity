import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that Metoprolol Succinate ER 50mg tablet refill was approved with modified refills set to 3."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Check refillRequests for Metoprolol Succinate ER 50mg tablet
    refill_requests = state.get("refillRequests", [])
    metoprolol_refill = None
    for rr in refill_requests:
        if rr.get("medicationName") == "Metoprolol Succinate ER 50mg tablet":
            metoprolol_refill = rr
            break

    if metoprolol_refill is None:
        return False, "No refill request found with medicationName='Metoprolol Succinate ER 50mg tablet'"

    # Check status is approved
    status = metoprolol_refill.get("status")
    if status != "approved":
        return False, f"Refill request status is '{status}', expected 'approved'"

    # Check linked medication in permanentRxMeds has refillsRemaining=3
    permanent_rx_meds = state.get("permanentRxMeds", [])
    metoprolol_med = None
    for med in permanent_rx_meds:
        if med.get("medicationName") == "Metoprolol Succinate ER 50mg tablet":
            metoprolol_med = med
            break

    if metoprolol_med is None:
        return False, "No medication found with medicationName='Metoprolol Succinate ER 50mg tablet' in permanentRxMeds"

    refills_remaining = metoprolol_med.get("refillsRemaining")
    if refills_remaining != 3:
        return False, f"refillsRemaining is {refills_remaining}, expected 3"

    return True, (
        f"Metoprolol Succinate ER 50mg tablet refill approved with refillsRemaining={refills_remaining}"
    )
