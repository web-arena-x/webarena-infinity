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
    perm_names = [m.get("medicationName", "") for m in permanent_rx_meds]

    # Check Losartan 50mg is discontinued
    losartan_name = "Losartan 50mg tablet"
    if losartan_name in perm_names:
        return False, f"'{losartan_name}' still found in permanentRxMeds, expected it to be discontinued"

    losartan_disc = None
    for med in discontinued_meds:
        if med.get("medicationName") == losartan_name:
            losartan_disc = med
            break
    if losartan_disc is None:
        return False, f"'{losartan_name}' not found in discontinuedMeds"

    # Check Amlodipine 5mg is discontinued
    amlodipine_name = "Amlodipine 5mg tablet"
    if amlodipine_name in perm_names:
        return False, f"'{amlodipine_name}' still found in permanentRxMeds, expected it to be discontinued"

    amlodipine_disc = None
    for med in discontinued_meds:
        if med.get("medicationName") == amlodipine_name:
            amlodipine_disc = med
            break
    if amlodipine_disc is None:
        return False, f"'{amlodipine_name}' not found in discontinuedMeds"

    # Check Valsartan 160mg prescribed
    valsartan = None
    for med in permanent_rx_meds:
        name = med.get("medicationName", "").lower()
        if "valsartan" in name and "160mg" in name:
            valsartan = med
            break

    if valsartan is None:
        return False, "No Valsartan 160mg medication found in permanentRxMeds"

    qty = valsartan.get("qty")
    if qty != 30:
        return False, f"Valsartan qty is {qty}, expected 30"

    refills = valsartan.get("refills", valsartan.get("refillsRemaining"))
    if refills != 3:
        return False, f"Valsartan refills/refillsRemaining is {refills}, expected 3"

    pharmacy_id = valsartan.get("pharmacyId", "")
    pharmacy_name = valsartan.get("pharmacyName", "")
    if pharmacy_id != "pharm_001" and "cvs" not in pharmacy_name.lower():
        return False, f"Valsartan pharmacy is '{pharmacy_name}' ({pharmacy_id}), expected CVS Pharmacy #4521 (pharm_001)"

    return True, "Losartan and Amlodipine discontinued, Valsartan 160mg prescribed: qty 30, 3 refills, CVS #4521"
