import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Step 1: PYUSD should be fully sold (quantity ~0)
    crypto_holdings = state.get("cryptoHoldings", [])
    pyusd = None
    for c in crypto_holdings:
        if c.get("symbol") == "PYUSD":
            pyusd = c
            break

    if pyusd is None:
        errors.append("PYUSD not found in crypto holdings.")
    else:
        if pyusd.get("quantity", 250) > 0.01:
            errors.append(
                f"PYUSD quantity is {pyusd.get('quantity')}, expected ~0 after selling all."
            )

    # Step 2: PayPal Credit should have decreased by $200
    credit = state.get("paypalCredit", {})
    expected_credit = 1245.67 - 200
    if abs(credit.get("currentBalance", 0) - expected_credit) > 1.0:
        errors.append(
            f"PayPal Credit balance is {credit.get('currentBalance')}, "
            f"expected ~{expected_credit} after $200 payment."
        )
    if credit.get("lastPaymentAmount") != 200:
        errors.append(
            f"Last payment amount is {credit.get('lastPaymentAmount')}, expected 200."
        )

    # Step 3: ATM limit should be $600
    debit = state.get("paypalDebitCard", {})
    if debit.get("dailyATMLimit") != 600:
        errors.append(
            f"Debit card ATM limit is {debit.get('dailyATMLimit')}, expected 600."
        )

    if errors:
        return False, " ".join(errors)
    return True, "Sold all PYUSD, made $200 credit payment, set ATM limit to $600."
