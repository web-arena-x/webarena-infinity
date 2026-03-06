import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Check permanentRxMeds for Famotidine 20mg
    permanent_rx_meds = state.get("permanentRxMeds", [])
    famotidine_med = None
    for med in permanent_rx_meds:
        name = med.get("medicationName", "").lower()
        if "famotidine" in name and "20mg" in name:
            famotidine_med = med
            break

    if famotidine_med is None:
        return False, "No medication containing 'Famotidine' and '20mg' found in permanentRxMeds"

    # Check qty == 30
    qty = famotidine_med.get("qty")
    if qty != 30:
        return False, f"Famotidine qty is {qty}, expected 30"

    # Check refills == 3 or refillsRemaining == 3
    refills = famotidine_med.get("refills")
    refills_remaining = famotidine_med.get("refillsRemaining")
    if refills != 3 and refills_remaining != 3:
        return False, f"Famotidine refills is {refills} and refillsRemaining is {refills_remaining}, expected one of them to be 3"

    # Check pharmacy is CVS #4521 (pharm_001)
    pharmacy_id = famotidine_med.get("pharmacyId", "")
    pharmacy_name = famotidine_med.get("pharmacyName", "")
    is_cvs = (
        pharmacy_id == "pharm_001"
        or ("cvs" in pharmacy_name.lower() and "4521" in pharmacy_name)
    )
    if not is_cvs:
        return False, f"Famotidine pharmacy is '{pharmacy_name}' ({pharmacy_id}), expected CVS #4521 (pharm_001)"

    return True, "Famotidine 20mg prescribed with qty 30, 3 refills, sent to CVS #4521"
