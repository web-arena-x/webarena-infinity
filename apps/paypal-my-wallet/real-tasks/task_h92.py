import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Step 1: Savings should have decreased by $2000
    savings = state.get("savingsAccount")
    if savings is None:
        errors.append("Savings account not found.")
    else:
        expected_savings = 12450.82 - 2000
        if abs(savings.get("balance", 0) - expected_savings) > 1.0:
            errors.append(
                f"Savings balance is {savings.get('balance')}, expected ~{expected_savings} "
                f"after withdrawing $2000."
            )

    # Step 2: BTC quantity should have increased (bought $500)
    crypto_holdings = state.get("cryptoHoldings", [])
    btc = None
    for c in crypto_holdings:
        if c.get("symbol") == "BTC":
            btc = c
            break

    if btc is None:
        errors.append("Bitcoin not found in crypto holdings.")
    else:
        if btc.get("quantity", 0) <= 0.04521:
            errors.append(
                f"BTC quantity is {btc.get('quantity')}, expected > 0.04521 after buying $500."
            )

    # Step 3: ETH quantity should have increased (bought $500)
    eth = None
    for c in crypto_holdings:
        if c.get("symbol") == "ETH":
            eth = c
            break

    if eth is None:
        errors.append("Ethereum not found in crypto holdings.")
    else:
        if eth.get("quantity", 0) <= 0.85200:
            errors.append(
                f"ETH quantity is {eth.get('quantity')}, expected > 0.85200 after buying $500."
            )

    # Step 4: PayPal Credit should have decreased by $500
    credit = state.get("paypalCredit", {})
    expected_credit = 1245.67 - 500
    if abs(credit.get("currentBalance", 0) - expected_credit) > 1.0:
        errors.append(
            f"PayPal Credit balance is {credit.get('currentBalance')}, "
            f"expected ~{expected_credit} after $500 payment."
        )

    if errors:
        return False, " ".join(errors)
    return True, "Withdrew $2000 from savings, bought $500 BTC, $500 ETH, paid $500 on credit."
