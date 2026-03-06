import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Check Ciprofloxacin is NOT in temporaryMeds
    temporary_meds = state.get("temporaryMeds", [])
    for med in temporary_meds:
        if "ciprofloxacin" in med.get("medicationName", "").lower():
            return False, "Ciprofloxacin still found in temporaryMeds, expected it to be moved to permanent"

    # Check Ciprofloxacin IS in permanentRxMeds
    permanent_rx_meds = state.get("permanentRxMeds", [])
    cipro_entries = [
        med for med in permanent_rx_meds
        if "ciprofloxacin" in med.get("medicationName", "").lower()
        and "500mg" in med.get("medicationName", "").lower()
    ]

    if len(cipro_entries) == 0:
        return False, "No Ciprofloxacin 500mg found in permanentRxMeds"

    # Check at least one Ciprofloxacin entry has Rite Aid pharmacy and qty 14
    rite_aid_cipro = None
    for med in cipro_entries:
        pharmacy_id = med.get("pharmacyId", "")
        pharmacy_name = med.get("pharmacyName", "")
        if pharmacy_id == "pharm_005" or "rite aid" in pharmacy_name.lower():
            if med.get("qty") == 14:
                rite_aid_cipro = med
                break

    if rite_aid_cipro is None:
        return False, "No Ciprofloxacin 500mg in permanentRxMeds with pharmacyId 'pharm_005' (Rite Aid) and qty 14"

    return True, "Ciprofloxacin moved to permanent and refilled at Rite Aid with qty 14"
