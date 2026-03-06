import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Check Melatonin is NOT in permanentOtcMeds
    permanent_otc_meds = state.get("permanentOtcMeds", [])
    for med in permanent_otc_meds:
        if med.get("medicationName") == "Melatonin 3mg tablet":
            return False, "Melatonin 3mg tablet still present in permanentOtcMeds"

    # Check Melatonin IS in discontinuedMeds
    discontinued_meds = state.get("discontinuedMeds", [])
    melatonin_discontinued = None
    for med in discontinued_meds:
        if med.get("medicationName") == "Melatonin 3mg tablet":
            melatonin_discontinued = med
            break

    if melatonin_discontinued is None:
        return False, "Melatonin 3mg tablet not found in discontinuedMeds"

    if melatonin_discontinued.get("status") != "discontinued":
        return False, f"Melatonin discontinued entry status is '{melatonin_discontinued.get('status')}', expected 'discontinued'"

    return True, "Melatonin 3mg tablet discontinued successfully"
