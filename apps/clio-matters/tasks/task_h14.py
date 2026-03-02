import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Find the DeLuca Felony DUI matter
    matters = state.get("matters", [])
    deluca = None
    for m in matters:
        desc = m.get("description", "").lower()
        if "deluca" in desc and ("felony dui" in desc or "third offense" in desc):
            deluca = m
            break

    if deluca is None:
        # Try matching by matter_48 as fallback
        deluca = next((m for m in matters if m.get("id") == "matter_48"), None)

    if deluca is None:
        return False, "Could not find DeLuca Felony DUI matter (description containing 'DeLuca' and 'Felony DUI' or 'third offense')."

    # Check 1: billingMethod == "flat_rate"
    if deluca.get("billingMethod") != "flat_rate":
        errors.append(
            f"billingMethod is '{deluca.get('billingMethod')}', expected 'flat_rate'."
        )

    # Check 2: billing.method == "flat_rate"
    billing = deluca.get("billing", {})
    if billing.get("method") != "flat_rate":
        errors.append(
            f"billing.method is '{billing.get('method')}', expected 'flat_rate'."
        )

    # Check 3: billing.flatRate is not null and amount == 15000
    flat_rate = billing.get("flatRate")
    if flat_rate is None:
        errors.append("billing.flatRate is null or missing.")
    else:
        amount = flat_rate.get("amount", 0)
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            amount = 0
        if abs(amount - 15000) > 500:
            errors.append(
                f"billing.flatRate.amount is {amount}, expected close to 15000."
            )

    # Check 4: stageId == "stage_3_2" (Pre-Trial)
    if deluca.get("stageId") != "stage_3_2":
        errors.append(
            f"stageId is '{deluca.get('stageId')}', expected 'stage_3_2' (Pre-Trial)."
        )

    if errors:
        return False, "DeLuca matter not updated correctly. " + " | ".join(errors)

    return True, "DeLuca matter updated to flat_rate billing at $15,000 and moved to Pre-Trial stage."
