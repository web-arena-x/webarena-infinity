import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Find Washington workplace injury matter
    matters = state.get("matters", [])
    washington = None
    for m in matters:
        desc = m.get("description", "").lower()
        if "washington" in desc and ("pacific steel" in desc or "crush" in desc):
            washington = m
            break

    if washington is None:
        return False, "Could not find Washington workplace injury matter (description containing 'Washington' and 'Pacific Steel' or 'crush')."

    matter_id = washington["id"]

    # Check 1: billing.contingencyFee.percentage close to 35
    billing = washington.get("billing", {})
    contingency_fee = billing.get("contingencyFee", {})
    if contingency_fee is None:
        contingency_fee = {}
    percentage = contingency_fee.get("percentage", 0)
    try:
        percentage = float(percentage)
    except (TypeError, ValueError):
        percentage = 0
    if abs(percentage - 35) > 1:
        errors.append(
            f"billing.contingencyFee.percentage is {percentage}, expected close to 35."
        )

    # Check 2: settlement has a recovery with amount close to 120000
    settlements = state.get("settlements", {})
    settlement = settlements.get(matter_id)
    if settlement is None:
        errors.append(f"No settlement found for Washington matter ({matter_id}).")
    else:
        recoveries = settlement.get("recoveries", [])
        has_recovery = any(
            abs(float(r.get("amount", 0)) - 120000) < 5000
            for r in recoveries
        )
        if not has_recovery:
            recovery_amounts = [r.get("amount") for r in recoveries]
            errors.append(
                f"No recovery with amount close to $120,000 found. "
                f"Recovery amounts: {recovery_amounts}."
            )

    # Check 3: stageId == "stage_1_5" (Settlement/Trial)
    if washington.get("stageId") != "stage_1_5":
        errors.append(
            f"stageId is '{washington.get('stageId')}', expected 'stage_1_5' (Settlement/Trial)."
        )

    if errors:
        return False, "Washington matter not updated correctly. " + " | ".join(errors)

    return True, "Washington matter updated: 35% contingency fee, $120,000 recovery added, moved to Settlement/Trial."
