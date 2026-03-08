import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Step 1: Savings should have decreased by $141.75 (Nike plan: 3 unpaid x $47.25)
    savings = state.get("savingsAccount")
    if savings is None:
        errors.append("Savings account not found.")
    else:
        expected_savings = 12450.82 - 141.75
        if abs(savings.get("balance", 0) - expected_savings) > 1.0:
            errors.append(
                f"Savings balance is {savings.get('balance')}, expected ~{expected_savings} "
                f"after withdrawing $141.75."
            )

    # Step 2: Should have a savings_withdrawal transaction
    transactions = state.get("transactions", [])
    found_withdrawal = any(
        t.get("type") == "savings_withdrawal"
        for t in transactions
        if t.get("id", "") not in {"txn_017"}
    )
    if not found_withdrawal:
        errors.append("No new savings_withdrawal transaction found.")

    # Step 3: EUR balance should have increased (converted $70 USD to EUR)
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
            f"EUR balance is {eur.get('amount')}, expected > 523.18 after converting $70."
        )

    # Step 4: Should have a currency_convert transaction to EUR
    found_convert = any(
        t.get("type") == "currency_convert" and "EUR" in (t.get("description") or "")
        for t in transactions
    )
    if not found_convert:
        errors.append("No currency_convert transaction to EUR found.")

    if errors:
        return False, " ".join(errors)
    return True, "Withdrew $141.75 (Nike plan remaining) from savings and converted $70 to EUR."
