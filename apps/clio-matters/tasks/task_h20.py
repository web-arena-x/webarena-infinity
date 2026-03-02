import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Find Fitzgerald medical malpractice matter
    matters = state.get("matters", [])
    fitzgerald = None
    for m in matters:
        desc = m.get("description", "").lower()
        if "fitzgerald" in desc and ("misdiagnosis" in desc or "breast cancer" in desc or "st. mary" in desc):
            fitzgerald = m
            break

    if fitzgerald is None:
        return False, "Could not find Fitzgerald matter (description containing 'Fitzgerald' and 'Misdiagnosis' or 'breast cancer' or 'St. Mary')."

    matter_id = fitzgerald["id"]

    # Check settlements
    settlements = state.get("settlements", {})
    settlement = settlements.get(matter_id)
    if settlement is None:
        return False, f"No settlement found for Fitzgerald matter ({matter_id})."

    # Check 1: recovery with amount close to 375000
    recoveries = settlement.get("recoveries", [])
    has_recovery = any(
        abs(float(r.get("amount", 0)) - 375000) < 15000
        for r in recoveries
    )
    if not has_recovery:
        recovery_amounts = [r.get("amount") for r in recoveries]
        errors.append(
            f"No recovery with amount close to $375,000 found. "
            f"Recovery amounts: {recovery_amounts}."
        )

    # Check 2: legalFees entry with percentage close to 40
    legal_fees = settlement.get("legalFees", [])
    has_legal_fee = any(
        abs(float(lf.get("percentage", 0)) - 40) < 2
        for lf in legal_fees
    )
    if not has_legal_fee:
        fee_percentages = [lf.get("percentage") for lf in legal_fees]
        errors.append(
            f"No legal fee with percentage close to 40% found. "
            f"Fee percentages: {fee_percentages}."
        )

    # Check 3: nonMedicalLiens entry with amount close to 20000
    non_medical_liens = settlement.get("nonMedicalLiens", [])
    has_lien = any(
        abs(float(l.get("amount", 0)) - 20000) < 3000
        for l in non_medical_liens
    )
    if not has_lien:
        lien_amounts = [l.get("amount") for l in non_medical_liens]
        errors.append(
            f"No non-medical lien with amount close to $20,000 found. "
            f"Lien amounts: {lien_amounts}."
        )

    # Check 4: outstandingBalances entry with originalAmount close to 5000
    outstanding = settlement.get("outstandingBalances", [])
    has_outstanding = any(
        abs(float(ob.get("originalAmount", 0)) - 5000) < 1500
        for ob in outstanding
    )
    if not has_outstanding:
        ob_amounts = [ob.get("originalAmount") for ob in outstanding]
        errors.append(
            f"No outstanding balance with originalAmount close to $5,000 found. "
            f"Outstanding balance amounts: {ob_amounts}."
        )

    if errors:
        return False, "Fitzgerald settlement not set up correctly. " + " | ".join(errors)

    return True, "Fitzgerald settlement correctly configured with $375,000 recovery, 40% legal fee, $20,000 non-medical lien, and $5,000 outstanding balance."
