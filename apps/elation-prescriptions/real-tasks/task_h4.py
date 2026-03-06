import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    calcium_name = "Calcium 600mg + Vitamin D3 400 IU tablet"

    # Check Calcium+D3 is NOT in permanentOtcMeds
    otc_meds = state.get("permanentOtcMeds", [])
    for med in otc_meds:
        if med.get("medicationName") == calcium_name:
            return False, f"'{calcium_name}' still found in permanentOtcMeds, expected it to be removed"

    # Check Calcium+D3 IS in discontinuedMeds
    discontinued_meds = state.get("discontinuedMeds", [])
    calcium_disc = None
    for med in discontinued_meds:
        if med.get("medicationName") == calcium_name:
            calcium_disc = med
            break

    if calcium_disc is None:
        return False, f"'{calcium_name}' not found in discontinuedMeds"

    if calcium_disc.get("status") != "discontinued":
        return False, f"'{calcium_name}' in discontinuedMeds has status '{calcium_disc.get('status')}', expected 'discontinued'"

    # Check lastReconciledDate has changed from seed value
    patient = state.get("currentPatient", {})
    last_reconciled = patient.get("lastReconciledDate", "")
    seed_reconciled = "2026-01-15T14:30:00Z"
    if last_reconciled == seed_reconciled:
        return False, f"lastReconciledDate is still the seed value '{seed_reconciled}', expected it to be updated after reconciliation"

    if not last_reconciled:
        return False, "lastReconciledDate is empty, expected it to be set after reconciliation"

    return True, "Med reconciliation completed: Calcium+D3 discontinued and lastReconciledDate updated"
