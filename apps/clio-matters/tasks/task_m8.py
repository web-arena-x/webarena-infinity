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

    liens = settlement.get("nonMedicalLiens", [])
    matching = [l for l in liens if abs(l.get("amount", 0) - 15000) < 1]

    if not matching:
        lien_amounts = [l.get("amount") for l in liens]
        return False, f"No non-medical lien with amount $15,000 found. Existing lien amounts: {lien_amounts}."

    return True, "Patterson settlement has a $15,000 non-medical lien entry."
