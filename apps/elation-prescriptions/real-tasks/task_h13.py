import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Check Sertraline refill request is approved
    refill_requests = state.get("refillRequests", [])
    sertraline_refill = None
    for req in refill_requests:
        if req.get("id") == "rr_007" or req.get("medicationName") == "Sertraline 50mg tablet":
            sertraline_refill = req
            break

    if sertraline_refill is None:
        return False, "Sertraline refill request (rr_007) not found in refillRequests"

    if sertraline_refill.get("status") != "approved":
        return False, f"Sertraline refill status is '{sertraline_refill.get('status')}', expected 'approved'"

    # Check Sertraline 100mg exists in permanentRxMeds
    permanent_rx_meds = state.get("permanentRxMeds", [])
    sertraline_100 = None
    for med in permanent_rx_meds:
        name = med.get("medicationName", "").lower()
        if "sertraline" in name and "100mg" in name:
            sertraline_100 = med
            break

    if sertraline_100 is None:
        return False, "No Sertraline 100mg medication found in permanentRxMeds"

    pharmacy_id = sertraline_100.get("pharmacyId", "")
    pharmacy_name = sertraline_100.get("pharmacyName", "")
    if pharmacy_id != "pharm_003" and "walgreens" not in pharmacy_name.lower():
        return False, f"Sertraline 100mg pharmacy is '{pharmacy_name}' ({pharmacy_id}), expected Walgreens #7892 (pharm_003)"

    return True, "Sertraline refill approved and Sertraline 100mg prescribed at Walgreens"
