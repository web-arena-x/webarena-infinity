import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify medication reconciliation with Aspirin 81mg discontinued."""
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

    # Check Aspirin 81mg is NOT in permanentOtcMeds
    permanent_otc_meds = state.get("permanentOtcMeds", [])
    aspirin_target = "Aspirin 81mg tablet (low-dose)"
    aspirin_in_otc = [
        m for m in permanent_otc_meds
        if m.get("medicationName") == aspirin_target
    ]

    if aspirin_in_otc:
        errors.append(
            f"'{aspirin_target}' still exists in permanentOtcMeds, expected it to be removed"
        )

    # Check Aspirin 81mg IS in discontinuedMeds
    discontinued_meds = state.get("discontinuedMeds", [])
    aspirin_in_disc = [
        m for m in discontinued_meds
        if m.get("medicationName") == aspirin_target
    ]

    if not aspirin_in_disc:
        disc_names = [m.get("medicationName", "") for m in discontinued_meds]
        errors.append(
            f"'{aspirin_target}' not found in discontinuedMeds. "
            f"Current discontinuedMeds: {disc_names}"
        )

    if errors:
        return False, (
            f"Medication reconciliation with Aspirin discontinuation issues: {'; '.join(errors)}"
        )

    return True, (
        f"Medication reconciliation completed. lastReconciledDate updated to "
        f"'{actual_reconciled_date}'. '{aspirin_target}' removed from permanentOtcMeds "
        f"and present in discontinuedMeds."
    )
