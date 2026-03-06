import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Check permanentRxMeds for Levothyroxine 50mcg
    permanent_rx_meds = state.get("permanentRxMeds", [])
    levo_med = None
    for med in permanent_rx_meds:
        name = med.get("medicationName", "").lower()
        if "levothyroxine" in name and "50" in name:
            levo_med = med
            break

    if levo_med is None:
        return False, "No medication containing 'Levothyroxine' and '50' found in permanentRxMeds"

    # Check qty == 30
    qty = levo_med.get("qty")
    if qty != 30:
        return False, f"Levothyroxine qty is {qty}, expected 30"

    # Check refills == 5 or refillsRemaining == 5
    refills = levo_med.get("refills")
    refills_remaining = levo_med.get("refillsRemaining")
    if refills != 5 and refills_remaining != 5:
        return False, f"Levothyroxine refills is {refills} and refillsRemaining is {refills_remaining}, expected one of them to be 5"

    # Check pharmacy is preferred (pharm_001 / CVS #4521)
    pharmacy_id = levo_med.get("pharmacyId", "")
    pharmacy_name = levo_med.get("pharmacyName", "")
    is_preferred = (
        pharmacy_id == "pharm_001"
        or ("cvs" in pharmacy_name.lower() and "4521" in pharmacy_name)
    )
    if not is_preferred:
        return False, f"Levothyroxine pharmacy is '{pharmacy_name}' ({pharmacy_id}), expected preferred pharmacy CVS #4521 (pharm_001)"

    return True, "Levothyroxine 50mcg prescribed with qty 30, 5 refills, to preferred pharmacy CVS #4521"
