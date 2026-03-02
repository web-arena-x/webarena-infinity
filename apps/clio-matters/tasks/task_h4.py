import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Find the Johnson v. Whole Foods matter
    matter = next(
        (m for m in state.get("matters", [])
         if "johnson" in m.get("description", "").lower()
         and "whole foods" in m.get("description", "").lower()),
        None
    )

    if matter is None:
        return False, "Could not find a matter with description containing 'Johnson' and 'Whole Foods'."

    matter_id = matter.get("id")
    description = matter.get("description", "")

    # Check settlements for this matter
    settlements = state.get("settlements", {})
    matter_settlement = settlements.get(matter_id, {})

    if not matter_settlement:
        return False, (
            f"No settlement data found for matter {matter_id} ('{description}'). "
            f"Available settlement keys: {list(settlements.keys())[:10]}."
        )

    # Check recovery with amount close to 208650
    recoveries = matter_settlement.get("recoveries", [])
    recovery_found = any(
        abs(float(r.get("amount", 0)) - 208650) < 500
        for r in recoveries
    )
    if not recovery_found:
        recovery_amounts = [r.get("amount") for r in recoveries]
        errors.append(
            f"No recovery entry found with amount close to $208,650. "
            f"Found recovery amounts: {recovery_amounts}."
        )

    # Check legal fee with percentage close to 33.33
    legal_fees = matter_settlement.get("legalFees", [])
    fee_found = any(
        abs(float(f.get("percentage", 0)) - 33.33) < 1
        for f in legal_fees
    )
    if not fee_found:
        fee_percentages = [f.get("percentage") for f in legal_fees]
        errors.append(
            f"No legal fee entry found with percentage close to 33.33%. "
            f"Found fee percentages: {fee_percentages}."
        )

    # Check non-medical lien with amount close to 14500
    non_medical_liens = matter_settlement.get("nonMedicalLiens", [])
    lien_found = any(
        abs(float(l.get("amount", 0)) - 14500) < 500
        for l in non_medical_liens
    )
    if not lien_found:
        lien_amounts = [l.get("amount") for l in non_medical_liens]
        errors.append(
            f"No non-medical lien entry found with amount close to $14,500. "
            f"Found lien amounts: {lien_amounts}."
        )

    if errors:
        return False, (
            f"Johnson v. Whole Foods settlement ({matter_id}) not set up correctly. "
            + " | ".join(errors)
        )

    return True, (
        f"Johnson v. Whole Foods matter ({matter_id}) settlement configured correctly: "
        f"recovery ~$208,650, legal fee ~33.33%, non-medical lien ~$14,500."
    )
