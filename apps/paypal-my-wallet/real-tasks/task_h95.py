import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Step 1: Notification settings
    notifs = state.get("walletPreferences", {}).get("emailNotifications", {})
    expected_notifs = {
        "payments": False,
        "transfers": False,
        "securityAlerts": True,
        "promotions": False,
        "cryptoAlerts": True,
        "rewardsUpdates": False,
        "weeklyDigest": False,
    }
    for key, expected_val in expected_notifs.items():
        actual_val = notifs.get(key)
        if actual_val != expected_val:
            errors.append(
                f"Notification '{key}' is {actual_val}, expected {expected_val}."
            )

    # Step 2: Cash back category should be Apparel
    debit = state.get("paypalDebitCard", {})
    if debit.get("cashBackCategory") != "Apparel":
        errors.append(
            f"Cash back category is '{debit.get('cashBackCategory')}', expected 'Apparel'."
        )

    # Step 3: Daily spending limit should be $4000
    if debit.get("dailySpendingLimit") != 4000:
        errors.append(
            f"Daily spending limit is {debit.get('dailySpendingLimit')}, expected 4000."
        )

    if errors:
        return False, " ".join(errors)
    return True, "Set notifications to security+crypto only, cash back to Apparel, spending limit $4000."
