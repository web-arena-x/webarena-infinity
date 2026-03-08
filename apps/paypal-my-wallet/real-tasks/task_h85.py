import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    bank_accounts = state.get("bankAccounts", [])
    remaining_last_fours = {b.get("lastFour") for b in bank_accounts}

    # Confirmed + instant transfer banks: Chase 6742 (added 2019-03-14), Citibank 1104 (added 2021-07-08)
    # Most recently added = Citibank 1104. Should be removed.
    if "1104" in remaining_last_fours:
        errors.append(
            "Citibank 1104 should have been removed (most recently added confirmed "
            "instant-transfer bank)."
        )

    # Other banks should remain
    for lf in ["6742", "3891", "5518", "7823"]:
        if lf not in remaining_last_fours:
            errors.append(f"Bank account ending in {lf} was removed but should have been kept.")

    if errors:
        return False, " ".join(errors)
    return True, "Removed Citibank 1104 (most recently added confirmed instant-transfer bank)."
