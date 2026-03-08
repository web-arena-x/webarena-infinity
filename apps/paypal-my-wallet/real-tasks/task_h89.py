import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Seed USD balance is $2847.63 > $2500, so agent should convert $500 to JPY directly.

    # Step 1: JPY balance should have increased
    balances = state.get("balances", [])
    jpy = None
    for b in balances:
        if b.get("currency") == "JPY":
            jpy = b
            break

    if jpy is None:
        errors.append("JPY balance not found.")
    elif jpy.get("amount", 0) <= 45200:
        errors.append(
            f"JPY balance is {jpy.get('amount')}, expected > 45200 after converting $500."
        )

    # Step 2: Should have a currency_convert transaction to JPY
    transactions = state.get("transactions", [])
    found_convert = any(
        t.get("type") == "currency_convert" and "JPY" in (t.get("description") or "")
        for t in transactions
    )
    if not found_convert:
        errors.append("No currency_convert transaction to JPY found.")

    # Step 3: Debit card cash back category should be Fuel
    debit = state.get("paypalDebitCard", {})
    if debit.get("cashBackCategory") != "Fuel":
        errors.append(
            f"Cash back category is '{debit.get('cashBackCategory')}', expected 'Fuel'."
        )

    if errors:
        return False, " ".join(errors)
    return True, "Converted $500 to JPY (balance was above $2500) and set cash back to Fuel."
