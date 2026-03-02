import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    matter = next(
        (m for m in state.get("matters", [])
         if "Patterson" in m.get("description", "") and "Metro Transit" in m.get("description", "")),
        None
    )

    if matter is None:
        return False, "Could not find a matter with description containing 'Patterson' and 'Metro Transit'."

    matter_id = matter.get("id")
    settlements = state.get("settlements", {})
    settlement = settlements.get(matter_id)

    if settlement is None:
        return False, f"No settlement found for matter '{matter_id}' (Patterson v. Metro Transit)."

    outstanding_balances = settlement.get("outstandingBalances", [])
    match = next(
        (ob for ob in outstanding_balances
         if ob.get("originalAmount") is not None and abs(ob.get("originalAmount", 0) - 5000) < 1),
        None
    )

    if match is None:
        summary = [(ob.get("creditor"), ob.get("originalAmount")) for ob in outstanding_balances]
        return False, f"No outstanding balance with originalAmount $5,000 found for Patterson settlement. Existing balances: {summary}."

    return True, "Patterson v. Metro Transit settlement has an outstanding balance with originalAmount $5,000."
