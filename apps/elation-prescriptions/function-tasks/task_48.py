import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify medication reconciliation completed without changes."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    current_patient = state.get("currentPatient", {})
    errors = []

    # Check lastReconciledDate changed from seed value
    seed_reconciled_date = "2026-01-15T14:30:00Z"
    actual_reconciled_date = current_patient.get("lastReconciledDate")

    if actual_reconciled_date == seed_reconciled_date:
        errors.append(
            f"lastReconciledDate is still the seed value '{seed_reconciled_date}', "
            f"expected it to be updated after reconciliation"
        )

    if not actual_reconciled_date:
        errors.append("lastReconciledDate is not set")

    # Check medication counts match seed data
    permanent_rx_count = len(state.get("permanentRxMeds", []))
    if permanent_rx_count != 11:
        errors.append(
            f"permanentRxMeds count: expected 11 (unchanged), got {permanent_rx_count}"
        )

    permanent_otc_count = len(state.get("permanentOtcMeds", []))
    if permanent_otc_count != 6:
        errors.append(
            f"permanentOtcMeds count: expected 6 (unchanged), got {permanent_otc_count}"
        )

    temporary_count = len(state.get("temporaryMeds", []))
    if temporary_count != 3:
        errors.append(
            f"temporaryMeds count: expected 3 (unchanged), got {temporary_count}"
        )

    if errors:
        return False, (
            f"Medication reconciliation issues: {'; '.join(errors)}"
        )

    return True, (
        f"Medication reconciliation completed without changes. "
        f"lastReconciledDate updated to '{actual_reconciled_date}'. "
        f"Med counts unchanged: permanentRxMeds={permanent_rx_count}, "
        f"permanentOtcMeds={permanent_otc_count}, temporaryMeds={temporary_count}."
    )
