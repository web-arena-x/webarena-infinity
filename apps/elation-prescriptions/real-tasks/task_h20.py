import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    otc_meds = state.get("permanentOtcMeds", [])
    discontinued_meds = state.get("discontinuedMeds", [])
    otc_names = [m.get("medicationName", "") for m in otc_meds]

    centrum_name = "Centrum Silver Multivitamin tablet"
    melatonin_name = "Melatonin 3mg tablet"

    # Check Centrum Silver NOT in permanentOtcMeds
    if centrum_name in otc_names:
        return False, f"'{centrum_name}' still found in permanentOtcMeds, expected it to be discontinued"

    # Check Centrum Silver IS in discontinuedMeds
    centrum_disc = None
    for med in discontinued_meds:
        if med.get("medicationName") == centrum_name:
            centrum_disc = med
            break
    if centrum_disc is None:
        return False, f"'{centrum_name}' not found in discontinuedMeds"

    # Check Melatonin NOT in permanentOtcMeds
    if melatonin_name in otc_names:
        return False, f"'{melatonin_name}' still found in permanentOtcMeds, expected it to be discontinued"

    # Check Melatonin IS in discontinuedMeds
    melatonin_disc = None
    for med in discontinued_meds:
        if med.get("medicationName") == melatonin_name:
            melatonin_disc = med
            break
    if melatonin_disc is None:
        return False, f"'{melatonin_name}' not found in discontinuedMeds"

    # Check lastReconciledDate has changed
    patient = state.get("currentPatient", {})
    last_reconciled = patient.get("lastReconciledDate", "")
    seed_reconciled = "2026-01-15T14:30:00Z"
    if last_reconciled == seed_reconciled:
        return False, f"lastReconciledDate is still the seed value '{seed_reconciled}', expected it to be updated after reconciliation"

    if not last_reconciled:
        return False, "lastReconciledDate is empty, expected it to be set after reconciliation"

    return True, "Med reconciliation completed: Centrum Silver and Melatonin discontinued, lastReconciledDate updated"
