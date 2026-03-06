import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Check Atorvastatin substitution change request is approved
    change_requests = state.get("changeRequests", [])
    atorvastatin_cr = None
    for cr in change_requests:
        if cr.get("originalMedication") == "Atorvastatin 20mg tablet" or cr.get("id") == "cr_001":
            atorvastatin_cr = cr
            break

    if atorvastatin_cr is None:
        return False, "Atorvastatin change request (cr_001) not found in changeRequests"

    if atorvastatin_cr.get("status") != "approved":
        return False, f"Atorvastatin change request status is '{atorvastatin_cr.get('status')}', expected 'approved'"

    # Check Rosuvastatin 10mg exists in permanentRxMeds
    permanent_rx_meds = state.get("permanentRxMeds", [])
    rosuvastatin = None
    for med in permanent_rx_meds:
        name = med.get("medicationName", "").lower()
        if "rosuvastatin" in name and "10mg" in name:
            rosuvastatin = med
            break

    if rosuvastatin is None:
        return False, "No Rosuvastatin 10mg medication found in permanentRxMeds"

    qty = rosuvastatin.get("qty")
    if qty != 30:
        return False, f"Rosuvastatin qty is {qty}, expected 30"

    refills = rosuvastatin.get("refills", rosuvastatin.get("refillsRemaining"))
    if refills != 5:
        return False, f"Rosuvastatin refills/refillsRemaining is {refills}, expected 5"

    pharmacy_id = rosuvastatin.get("pharmacyId", "")
    pharmacy_name = rosuvastatin.get("pharmacyName", "")
    if pharmacy_id != "pharm_001" and "cvs" not in pharmacy_name.lower():
        return False, f"Rosuvastatin pharmacy is '{pharmacy_name}' ({pharmacy_id}), expected CVS Pharmacy #4521 (pharm_001)"

    return True, "Atorvastatin substitution approved and Rosuvastatin 10mg prescribed: qty 30, 5 refills, CVS #4521"
