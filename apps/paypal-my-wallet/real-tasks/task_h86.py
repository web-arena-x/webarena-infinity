import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Positive-return cryptos: BTC $3066.89, ETH $3018.47, LTC $515.28, BCH $343.97, LINK $234.38
    # Total = $7178.99, 5% = $358.95, rounded = $359

    savings = state.get("savingsAccount")
    if savings is None:
        errors.append("Savings account not found.")
    else:
        expected_savings = 12450.82 + 359
        if abs(savings.get("balance", 0) - expected_savings) > 2.0:
            errors.append(
                f"Savings balance is {savings.get('balance')}, expected ~{expected_savings} "
                f"after depositing $359 (5% of positive-return crypto value)."
            )

    # Should have a savings_deposit transaction
    transactions = state.get("transactions", [])
    found_deposit = any(
        t.get("type") == "savings_deposit"
        for t in transactions
        if t.get("id", "") not in {"txn_017"}
    )
    if not found_deposit:
        errors.append("No new savings_deposit transaction found.")

    if errors:
        return False, " ".join(errors)
    return True, "Deposited $359 (5% of $7,178.99 positive-return crypto value) into savings."
