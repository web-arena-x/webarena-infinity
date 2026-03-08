import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Highest total cost crypto: ETH at $1942.56

    # Step 1: ETH quantity should have decreased (sold $200)
    crypto_holdings = state.get("cryptoHoldings", [])
    eth = None
    for c in crypto_holdings:
        if c.get("symbol") == "ETH":
            eth = c
            break

    if eth is None:
        errors.append("Ethereum not found in crypto holdings.")
    else:
        if eth.get("quantity", 0) >= 0.85200:
            errors.append(
                f"ETH quantity is {eth.get('quantity')}, expected < 0.85200 after selling $200."
            )

    # Step 2: EUR balance should have increased ($100 converted)
    balances = state.get("balances", [])
    eur = None
    for b in balances:
        if b.get("currency") == "EUR":
            eur = b
            break

    if eur is None:
        errors.append("EUR balance not found.")
    elif eur.get("amount", 0) <= 523.18:
        errors.append(
            f"EUR balance is {eur.get('amount')}, expected > 523.18 after converting $100."
        )

    # Step 3: Savings should have increased by $100
    savings = state.get("savingsAccount")
    if savings is None:
        errors.append("Savings account not found.")
    else:
        expected_savings = 12450.82 + 100
        if abs(savings.get("balance", 0) - expected_savings) > 1.0:
            errors.append(
                f"Savings balance is {savings.get('balance')}, expected ~{expected_savings} "
                f"after depositing $100."
            )

    # Should have a crypto_sell transaction for Ethereum
    transactions = state.get("transactions", [])
    found_sell = any(
        t.get("type") == "crypto_sell" and "Ethereum" in (t.get("description") or "")
        for t in transactions
    )
    if not found_sell:
        errors.append("No crypto_sell transaction for Ethereum found.")

    if errors:
        return False, " ".join(errors)
    return True, "Sold $200 ETH (highest total cost), converted $100 to EUR, deposited $100 to savings."
