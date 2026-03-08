import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    cards = state.get("cards", [])
    remaining_last_fours = {c.get("lastFour") for c in cards}

    # Step 1: Expired (Discover 6221) and pending (Visa 8834) should be removed
    if "6221" in remaining_last_fours:
        errors.append("Expired Discover card 6221 should have been removed.")
    if "8834" in remaining_last_fours:
        errors.append("Pending Visa card 8834 should have been removed.")

    # Step 2: Remaining confirmed cards should be kept
    for lf in ["4829", "7156", "3001", "2290"]:
        if lf not in remaining_last_fours:
            errors.append(f"Card ending in {lf} was removed but should have been kept.")

    # Step 3: AmEx 3001 (last used 2026-01-15, earliest among remaining) should be preferred
    amex_3001 = None
    for c in cards:
        if c.get("lastFour") == "3001":
            amex_3001 = c
            break

    if amex_3001 is not None:
        if not amex_3001.get("isPreferred"):
            errors.append("AmEx 3001 should be set as preferred (earliest last used).")

    prefs = state.get("walletPreferences", {})
    if amex_3001 and prefs.get("preferredPaymentMethod") != amex_3001.get("id"):
        errors.append(
            f"Wallet preferred payment is '{prefs.get('preferredPaymentMethod')}', "
            f"expected '{amex_3001.get('id') if amex_3001 else 'card_003'}'."
        )

    # Step 4: No other card should be preferred
    for c in cards:
        if c.get("lastFour") != "3001" and c.get("isPreferred"):
            errors.append(
                f"Card {c.get('lastFour')} should not be preferred."
            )

    if errors:
        return False, " ".join(errors)
    return True, "Removed expired/pending cards and set AmEx 3001 (earliest last used) as preferred."
