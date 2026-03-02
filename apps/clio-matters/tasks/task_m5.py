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

    recoveries = settlement.get("recoveries", [])
    matching = [r for r in recoveries if abs(r.get("amount", 0) - 250000) < 1]

    if not matching:
        recovery_amounts = [r.get("amount") for r in recoveries]
        return False, f"No recovery with amount $250,000 found. Existing recovery amounts: {recovery_amounts}."

    return True, "Patterson settlement has a $250,000 recovery entry."
