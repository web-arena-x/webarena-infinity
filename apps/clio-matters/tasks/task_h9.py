import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Find the Okafor burn matter
    matter = next(
        (m for m in state.get("matters", [])
         if "okafor" in m.get("description", "").lower()
         and "burn" in m.get("description", "").lower()),
        None
    )

    if matter is None:
        return False, "Could not find a matter with description containing 'Okafor' and 'burn'."

    matter_id = matter.get("id")
    description = matter.get("description", "")

    # Check for a damage entry with amount close to 35000
    damages = state.get("damages", [])
    matter_damages = [d for d in damages if d.get("matterId") == matter_id]

    damage_found = any(
        abs(float(d.get("amount", 0)) - 35000) < 1000
        for d in matter_damages
    )

    if not damage_found:
        damage_amounts = [d.get("amount") for d in matter_damages]
        errors.append(
            f"No damage entry found for matter {matter_id} with amount close to $35,000. "
            f"Found damage amounts: {damage_amounts}."
        )

    # Check settlements for this matter
    settlements = state.get("settlements", {})
    matter_settlement = settlements.get(matter_id, {})

    # Check legal fee with percentage close to 40
    legal_fees = matter_settlement.get("legalFees", [])
    fee_found = any(
        abs(float(f.get("percentage", 0)) - 40) < 1
        for f in legal_fees
    )

    if not fee_found:
        fee_data = [
            {"percentage": f.get("percentage"), "flatAmount": f.get("flatAmount")}
            for f in legal_fees
        ]
        errors.append(
            f"No legal fee entry found for matter {matter_id} with percentage close to 40%. "
            f"Found legal fees: {fee_data}."
        )

    # Check outstanding balance with originalAmount close to 8000
    outstanding_balances = matter_settlement.get("outstandingBalances", [])
    balance_found = any(
        abs(float(b.get("originalAmount", 0)) - 8000) < 500
        for b in outstanding_balances
    )

    if not balance_found:
        balance_amounts = [b.get("originalAmount") for b in outstanding_balances]
        errors.append(
            f"No outstanding balance found for matter {matter_id} with originalAmount close to $8,000. "
            f"Found outstanding balance amounts: {balance_amounts}."
        )

    if errors:
        return False, (
            f"Okafor burn case ({matter_id}: '{description}') not set up correctly. "
            + " | ".join(errors)
        )

    return True, (
        f"Okafor burn case ({matter_id}) updated correctly: "
        f"damage ~$35,000, legal fee ~40%, outstanding balance ~$8,000."
    )
