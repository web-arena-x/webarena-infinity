import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    matter = next(
        (m for m in state.get("matters", [])
         if "Okafor" in m.get("description", "")
         and ("burn" in m.get("description", "").lower() or "HomeComfort" in m.get("description", ""))),
        None
    )

    if matter is None:
        return False, "Could not find a matter with description containing 'Okafor' and 'burn' or 'HomeComfort'."

    matter_id = matter.get("id")
    settlements = state.get("settlements", {})
    settlement = settlements.get(matter_id)

    if settlement is None:
        return False, f"No settlement found for matter '{matter_id}' (Okafor burn case)."

    legal_fees = settlement.get("legalFees", [])
    contingency_fee = next(
        (fee for fee in legal_fees
         if fee.get("percentage") is not None and abs(fee.get("percentage", 0) - 33.33) < 0.1),
        None
    )

    if contingency_fee is None:
        summary = [(f.get("type"), f.get("percentage"), f.get("flatAmount")) for f in legal_fees]
        return False, f"No legal fee with percentage ~33.33% found for Okafor burn case. Existing legal fees: {summary}."

    return True, "Okafor burn case settlement has a 33.33% contingency legal fee."
