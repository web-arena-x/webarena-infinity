import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Largest redemption in seed: rwd_008 = -1000 points = $10.00
    # Should have bought $10 of Solana

    crypto_holdings = state.get("cryptoHoldings", [])
    sol = None
    for c in crypto_holdings:
        if c.get("symbol") == "SOL":
            sol = c
            break

    if sol is None:
        errors.append("Solana not found in crypto holdings.")
    else:
        # Seed SOL quantity is 0. After buying $10, quantity should be > 0
        if sol.get("quantity", 0) <= 0:
            errors.append(
                f"Solana quantity is {sol.get('quantity')}, expected > 0 "
                f"after buying $10."
            )

    # USD balance should have decreased by ~$10
    balances = state.get("balances", [])
    usd = None
    for b in balances:
        if b.get("currency") == "USD":
            usd = b
            break

    if usd is None:
        errors.append("USD balance not found.")
    else:
        expected_usd = 2847.63 - 10
        if abs(usd.get("amount", 0) - expected_usd) > 2.0:
            errors.append(
                f"USD balance is {usd.get('amount')}, expected ~{expected_usd} "
                f"after buying $10 of Solana."
            )

    # Should have a crypto_buy transaction for Solana
    transactions = state.get("transactions", [])
    found_buy = any(
        t.get("type") == "crypto_buy" and "Solana" in (t.get("description") or "")
        for t in transactions
    )
    if not found_buy:
        errors.append("No crypto_buy transaction for Solana found.")

    if errors:
        return False, " ".join(errors)
    return True, "Bought $10 of Solana (matching largest historical redemption of $10)."
