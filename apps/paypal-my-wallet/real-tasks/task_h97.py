import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    balances = state.get("balances", [])

    # Step 1: CHF should exist with positive balance
    chf = None
    for b in balances:
        if b.get("currency") == "CHF":
            chf = b
            break

    if chf is None:
        errors.append("Swiss Franc (CHF) not found in balances.")
    elif chf.get("amount", 0) <= 0:
        errors.append(f"CHF balance is {chf.get('amount')}, expected > 0 after converting $400.")

    # Step 2: Currency conversion should be card_issuer
    prefs = state.get("walletPreferences", {})
    if prefs.get("currencyConversionOption") != "card_issuer":
        errors.append(
            f"Currency conversion is '{prefs.get('currencyConversionOption')}', "
            f"expected 'card_issuer'."
        )

    # Step 3: AmEx 3001 should be preferred
    cards = state.get("cards", [])
    amex = None
    for c in cards:
        if c.get("lastFour") == "3001":
            amex = c
            break

    if amex is None:
        errors.append("AmEx 3001 not found in cards.")
    else:
        if not amex.get("isPreferred"):
            errors.append("AmEx 3001 should be set as preferred.")

    if amex and prefs.get("preferredPaymentMethod") != amex.get("id"):
        errors.append(
            f"Wallet preferred payment is '{prefs.get('preferredPaymentMethod')}', "
            f"expected '{amex.get('id') if amex else 'card_003'}'."
        )

    # Step 4: Weekly digest should be disabled
    notifs = prefs.get("emailNotifications", {})
    if notifs.get("weeklyDigest") is not False:
        errors.append(
            f"Weekly digest is {notifs.get('weeklyDigest')}, expected False."
        )

    if errors:
        return False, " ".join(errors)
    return True, "Added CHF, converted $400, set card issuer, set AmEx preferred, disabled weekly digest."
