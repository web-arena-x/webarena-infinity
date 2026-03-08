import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    credit = state.get("paypalCredit", {})

    # Step 1: Autopay should be set to "full" (seed was "minimum")
    if credit.get("autopayAmount") != "full":
        errors.append(
            f"Autopay amount is '{credit.get('autopayAmount')}', expected 'full'."
        )

    # Step 2: Credit balance should have decreased by $250
    expected_balance = 1245.67 - 250
    if abs(credit.get("currentBalance", 0) - expected_balance) > 1.0:
        errors.append(
            f"PayPal Credit balance is {credit.get('currentBalance')}, "
            f"expected ~{expected_balance} after $250 payment."
        )

    if credit.get("lastPaymentAmount") != 250:
        errors.append(
            f"Last payment amount is {credit.get('lastPaymentAmount')}, expected 250."
        )

    if errors:
        return False, " ".join(errors)
    return True, "Changed autopay to full balance and made $250 credit payment."
