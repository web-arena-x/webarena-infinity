import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    permanent_rx_meds = state.get("permanentRxMeds", [])
    discontinued_meds = state.get("discontinuedMeds", [])

    omeprazole_name = "Omeprazole 20mg capsule"

    # Check Omeprazole is NOT in permanentRxMeds
    perm_names = [m.get("medicationName", "") for m in permanent_rx_meds]
    if omeprazole_name in perm_names:
        return False, f"'{omeprazole_name}' still found in permanentRxMeds, expected it to be discontinued"

    # Check Omeprazole IS in discontinuedMeds
    omeprazole_disc = None
    for med in discontinued_meds:
        if med.get("medicationName") == omeprazole_name:
            omeprazole_disc = med
            break
    if omeprazole_disc is None:
        return False, f"'{omeprazole_name}' not found in discontinuedMeds"

    # Check Famotidine 20mg prescribed
    famotidine = None
    for med in permanent_rx_meds:
        name = med.get("medicationName", "").lower()
        if "famotidine" in name and "20mg" in name:
            famotidine = med
            break

    if famotidine is None:
        return False, "No Famotidine 20mg medication found in permanentRxMeds"

    qty = famotidine.get("qty")
    if qty != 60:
        return False, f"Famotidine qty is {qty}, expected 60"

    refills = famotidine.get("refills", famotidine.get("refillsRemaining"))
    if refills != 3:
        return False, f"Famotidine refills/refillsRemaining is {refills}, expected 3"

    pharmacy_id = famotidine.get("pharmacyId", "")
    pharmacy_name = famotidine.get("pharmacyName", "")
    if pharmacy_id != "pharm_001" and "cvs" not in pharmacy_name.lower():
        return False, f"Famotidine pharmacy is '{pharmacy_name}' ({pharmacy_id}), expected CVS Pharmacy #4521 (pharm_001)"

    return True, "Omeprazole discontinued and Famotidine 20mg prescribed: qty 60, 3 refills, CVS #4521"
