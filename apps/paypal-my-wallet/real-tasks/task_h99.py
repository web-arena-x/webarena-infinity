import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    bank_accounts = state.get("bankAccounts", [])
    remaining_last_fours = {b.get("lastFour") for b in bank_accounts}

    # Step 1: Non-instant-transfer accounts should be removed (BofA 3891, US Bank 7823)
    if "3891" in remaining_last_fours:
        errors.append("Bank of America 3891 (no instant transfer) should have been removed.")
    if "7823" in remaining_last_fours:
        errors.append("US Bank 7823 (no instant transfer) should have been removed.")

    # Step 2: Instant-transfer accounts should remain
    for lf in ["6742", "5518", "1104"]:
        if lf not in remaining_last_fours:
            errors.append(
                f"Bank account ending in {lf} (instant transfer) was removed "
                f"but should have been kept."
            )

    # Step 3: USD balance should have increased by ~$200 ($100 from Chase + $100 from Citibank)
    balances = state.get("balances", [])
    usd = None
    for b in balances:
        if b.get("currency") == "USD":
            usd = b
            break

    if usd is None:
        errors.append("USD balance not found.")
    else:
        expected_usd = 2847.63 + 200
        if abs(usd.get("amount", 0) - expected_usd) > 2.0:
            errors.append(
                f"USD balance is {usd.get('amount')}, expected ~{expected_usd} "
                f"after adding $100 each from Chase and Citibank."
            )

    # Step 4: Should have transfer_in transactions from both Chase and Citibank
    transactions = state.get("transactions", [])
    chase_transfer = any(
        t.get("type") == "transfer_in" and "6742" in (t.get("description") or "")
        for t in transactions
        if t.get("id", "") != "txn_010"  # exclude seed transfer
    )
    citi_transfer = any(
        t.get("type") == "transfer_in" and "1104" in (t.get("description") or "")
        for t in transactions
    )

    if not chase_transfer:
        errors.append("No new transfer_in from Chase (6742) found.")
    if not citi_transfer:
        errors.append("No transfer_in from Citibank (1104) found.")

    if errors:
        return False, " ".join(errors)
    return True, "Removed non-instant-transfer banks, added $100 each from Chase and Citibank."
