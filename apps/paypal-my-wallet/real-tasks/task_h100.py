import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Crypto total value: BTC $3066.89 + ETH $3018.47 + LTC $515.28 + BCH $343.97 +
    # SOL $0 + LINK $234.38 + PYUSD $250.00 = $7428.99 > $7000
    # So: sell $300 of Bitcoin

    # Step 1: BTC quantity should have decreased
    crypto_holdings = state.get("cryptoHoldings", [])
    btc = None
    for c in crypto_holdings:
        if c.get("symbol") == "BTC":
            btc = c
            break

    if btc is None:
        errors.append("Bitcoin not found in crypto holdings.")
    else:
        if btc.get("quantity", 0) >= 0.04521:
            errors.append(
                f"BTC quantity is {btc.get('quantity')}, expected < 0.04521 "
                f"after selling $300 (portfolio > $7000)."
            )

    # Should have a crypto_sell transaction for Bitcoin
    transactions = state.get("transactions", [])
    found_sell = any(
        t.get("type") == "crypto_sell" and "Bitcoin" in (t.get("description") or "")
        for t in transactions
    )
    if not found_sell:
        errors.append("No crypto_sell transaction for Bitcoin found.")

    # Step 2: Daily spending limit should be $2500
    debit = state.get("paypalDebitCard", {})
    if debit.get("dailySpendingLimit") != 2500:
        errors.append(
            f"Daily spending limit is {debit.get('dailySpendingLimit')}, expected 2500."
        )

    if errors:
        return False, " ".join(errors)
    return True, "Sold $300 BTC (portfolio > $7000) and set spending limit to $2500."
