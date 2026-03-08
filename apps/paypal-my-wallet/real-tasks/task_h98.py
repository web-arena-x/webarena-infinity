import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # 25% of $1245.67 = $311.42, rounded = $311

    # Step 1: Credit balance should have decreased by $311
    credit = state.get("paypalCredit", {})
    expected_credit = 1245.67 - 311
    if abs(credit.get("currentBalance", 0) - expected_credit) > 2.0:
        errors.append(
            f"PayPal Credit balance is {credit.get('currentBalance')}, "
            f"expected ~{expected_credit} after paying $311 (25% of balance)."
        )

    if credit.get("lastPaymentAmount") != 311:
        errors.append(
            f"Last payment amount is {credit.get('lastPaymentAmount')}, expected 311."
        )

    # Step 2: Rewards should have decreased by 1000 points
    rewards = state.get("rewards", {})
    expected_points = 4825 - 1000
    if abs(rewards.get("totalPoints", 0) - expected_points) > 5:
        errors.append(
            f"Reward points are {rewards.get('totalPoints')}, expected ~{expected_points} "
            f"after redeeming 1000 points."
        )

    # Should have a redeemed entry in history
    history = rewards.get("history", [])
    found_redeem = any(
        h.get("type") == "redeemed" and h.get("points", 0) == -1000
        for h in history
    )
    if not found_redeem:
        errors.append("No redemption of 1000 points found in rewards history.")

    if errors:
        return False, " ".join(errors)
    return True, "Paid $311 (25% of credit balance) and redeemed 1000 reward points for balance."
