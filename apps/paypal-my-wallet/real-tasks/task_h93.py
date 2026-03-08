import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    bank_accounts = state.get("bankAccounts", [])
    remaining_last_fours = {b.get("lastFour") for b in bank_accounts}

    # Step 1: Savings-type accounts (BofA 3891, US Bank 7823) should be removed
    if "3891" in remaining_last_fours:
        errors.append("Bank of America 3891 (savings) should have been removed.")
    if "7823" in remaining_last_fours:
        errors.append("US Bank 7823 (savings) should have been removed.")

    # Step 2: Checking accounts should remain
    for lf in ["6742", "5518", "1104"]:
        if lf not in remaining_last_fours:
            errors.append(f"Checking account ending in {lf} was removed but should have been kept.")

    # Step 3: Citibank 1104 (lowest last four among checking) should be set as backup
    citi = None
    for b in bank_accounts:
        if b.get("lastFour") == "1104":
            citi = b
            break

    prefs = state.get("walletPreferences", {})
    if citi and prefs.get("backupPaymentMethod") != citi.get("id"):
        errors.append(
            f"Backup payment is '{prefs.get('backupPaymentMethod')}', "
            f"expected '{citi.get('id') if citi else 'bank_004'}' (Citibank 1104)."
        )

    user = state.get("currentUser", {})
    if citi and user.get("backupPaymentMethodId") != citi.get("id"):
        errors.append(
            f"User backup payment ID is '{user.get('backupPaymentMethodId')}', "
            f"expected '{citi.get('id') if citi else 'bank_004'}'."
        )

    if errors:
        return False, " ".join(errors)
    return True, "Removed savings bank accounts and set Citibank 1104 as backup."
