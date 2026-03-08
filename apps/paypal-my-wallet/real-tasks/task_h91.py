import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Total remaining across active plans:
    # Nordstrom: $71.12 + $71.12 = $142.24
    # Nike: $47.25 + $47.25 + $47.25 = $141.75
    # Total = $283.99

    # GBP balance should have increased
    balances = state.get("balances", [])
    gbp = None
    for b in balances:
        if b.get("currency") == "GBP":
            gbp = b
            break

    if gbp is None:
        errors.append("GBP balance not found.")
    elif gbp.get("amount", 0) <= 189.42:
        errors.append(
            f"GBP balance is {gbp.get('amount')}, expected > 189.42 after converting "
            f"$283.99 to GBP."
        )

    # USD balance should have decreased by ~$283.99
    usd = None
    for b in balances:
        if b.get("currency") == "USD":
            usd = b
            break

    if usd is None:
        errors.append("USD balance not found.")
    else:
        expected_usd = 2847.63 - 283.99
        if abs(usd.get("amount", 0) - expected_usd) > 2.0:
            errors.append(
                f"USD balance is {usd.get('amount')}, expected ~{expected_usd} "
                f"after converting $283.99."
            )

    # Should have a currency_convert transaction to GBP
    transactions = state.get("transactions", [])
    found_convert = any(
        t.get("type") == "currency_convert" and "GBP" in (t.get("description") or "")
        for t in transactions
    )
    if not found_convert:
        errors.append("No currency_convert transaction to GBP found.")

    if errors:
        return False, " ".join(errors)
    return True, "Converted $283.99 (total remaining Pay in 4 payments) to GBP."
