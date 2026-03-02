import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Find McCarthy pedestrian matter
    matters = state.get("matters", [])
    mccarthy = None
    for m in matters:
        desc = m.get("description", "").lower()
        if "mccarthy" in desc and ("pedestrian" in desc or "crosswalk" in desc):
            mccarthy = m
            break

    if mccarthy is None:
        return False, "Could not find McCarthy pedestrian matter (description containing 'McCarthy' and 'pedestrian' or 'crosswalk')."

    matter_id = mccarthy["id"]

    # Check settlements
    settlements = state.get("settlements", {})
    settlement = settlements.get(matter_id)
    if settlement is None:
        return False, f"No settlement found for McCarthy matter ({matter_id})."

    # Check recovery with amount close to 150000
    recoveries = settlement.get("recoveries", [])
    has_recovery = any(
        abs(float(r.get("amount", 0)) - 150000) < 5000
        for r in recoveries
    )
    if not has_recovery:
        recovery_amounts = [r.get("amount") for r in recoveries]
        errors.append(
            f"No recovery with amount close to $150,000 found. "
            f"Recovery amounts: {recovery_amounts}."
        )

    # Check legalFees entry with percentage close to 33.33
    legal_fees = settlement.get("legalFees", [])
    has_legal_fee = any(
        abs(float(lf.get("percentage", 0)) - 33.33) < 2
        for lf in legal_fees
    )
    if not has_legal_fee:
        fee_percentages = [lf.get("percentage") for lf in legal_fees]
        errors.append(
            f"No legal fee with percentage close to 33.33% found. "
            f"Fee percentages: {fee_percentages}."
        )

    # Check outstandingBalances entry with originalAmount close to 25000
    outstanding = settlement.get("outstandingBalances", [])
    has_outstanding = any(
        abs(float(ob.get("originalAmount", 0)) - 25000) < 3000
        for ob in outstanding
    )
    if not has_outstanding:
        ob_amounts = [ob.get("originalAmount") for ob in outstanding]
        errors.append(
            f"No outstanding balance with originalAmount close to $25,000 found. "
            f"Outstanding balance amounts: {ob_amounts}."
        )

    if errors:
        return False, "McCarthy settlement not set up correctly. " + " | ".join(errors)

    return True, "McCarthy pedestrian settlement correctly configured with $150,000 recovery, 33.33% legal fee, and $25,000 outstanding balance."
