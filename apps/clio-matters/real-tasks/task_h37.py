import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Find Harris matter
    harris = None
    for m in state.get("matters", []):
        if "Harris" in (m.get("description") or ""):
            harris = m
            break

    if not harris:
        return False, "Harris workplace injury matter not found."

    errors = []

    # Check contingency rate is 40%
    billing = harris.get("billingPreference", {})
    rate = billing.get("contingencyRate")
    if rate != 40:
        errors.append(f"Contingency rate is {rate}, expected 40")

    # Check new Disfigurement damage
    damages = harris.get("damages", [])
    disfigurement = [d for d in damages if d.get("type") == "Disfigurement"]
    if not disfigurement:
        errors.append("No 'Disfigurement' damage found")
    else:
        d = disfigurement[0]
        if d.get("amount") != 10000:
            errors.append(f"Disfigurement amount is {d.get('amount')}, expected 10000")
        if d.get("category") != "General":
            errors.append(f"Disfigurement category is '{d.get('category')}', expected 'General'")

    # Check stage is Demand Letter
    pi_pa = None
    for pa in state.get("practiceAreas", []):
        if pa.get("name") == "Personal Injury":
            pi_pa = pa
            break

    if pi_pa:
        stages = state.get("matterStages", {}).get(pi_pa["id"], [])
        demand_id = None
        for stg in stages:
            if stg.get("name") == "Demand Letter":
                demand_id = stg.get("id")
                break

        if demand_id and harris.get("matterStageId") != demand_id:
            errors.append(
                f"Harris stage is '{harris.get('matterStageId')}', "
                f"expected '{demand_id}' (Demand Letter)"
            )

    if errors:
        return False, "; ".join(errors)

    return True, "Harris: contingency 40%, Disfigurement $10k added, moved to Demand Letter."
