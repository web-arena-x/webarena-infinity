import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Smallest non-zero remaining gift card: Starbucks gc_002 = $12.50

    # Step 1: Rewards should have decreased by 1250 points (12.50 * 100)
    rewards = state.get("rewards", {})
    expected_points = 4825 - 1250
    if abs(rewards.get("totalPoints", 0) - expected_points) > 5:
        errors.append(
            f"Reward points are {rewards.get('totalPoints')}, expected ~{expected_points} "
            f"after redeeming 1250 points."
        )

    # Should have a redeemed entry in rewards history
    history = rewards.get("history", [])
    found_redeem = any(
        h.get("type") == "redeemed" and h.get("points", 0) == -1250
        for h in history
    )
    if not found_redeem:
        errors.append("No redemption of 1250 points found in rewards history.")

    # Step 2: Savings should have increased by $12.50
    savings = state.get("savingsAccount")
    if savings is None:
        errors.append("Savings account not found.")
    else:
        expected_savings = 12450.82 + 12.50
        if abs(savings.get("balance", 0) - expected_savings) > 1.0:
            errors.append(
                f"Savings balance is {savings.get('balance')}, expected ~{expected_savings} "
                f"after depositing $12.50."
            )

    if errors:
        return False, " ".join(errors)
    return True, "Redeemed 1250 points ($12.50) for balance and deposited $12.50 into savings."
