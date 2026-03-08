import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Check Workers Compensation is disabled
    wc_pa = None
    for pa in state.get("practiceAreas", []):
        if pa.get("name") == "Workers Compensation":
            wc_pa = pa
            break

    if not wc_pa:
        errors.append("Workers Compensation practice area not found")
    elif wc_pa.get("enabled") is not False:
        errors.append(
            f"Workers Compensation enabled is {wc_pa.get('enabled')}, expected False"
        )

    # Find PI practice area
    pi_pa = None
    for pa in state.get("practiceAreas", []):
        if pa.get("name") == "Personal Injury":
            pi_pa = pa
            break

    if not pi_pa:
        errors.append("Personal Injury practice area not found")

    # Find Demand Letter stage in PI
    demand_stage_id = None
    if pi_pa:
        pi_stages = state.get("matterStages", {}).get(pi_pa["id"], [])
        for stg in pi_stages:
            if stg.get("name") == "Demand Letter":
                demand_stage_id = stg.get("id")
                break

    # Find Kowalski matter
    kowalski = None
    for m in state.get("matters", []):
        if "Kowalski" in (m.get("description") or ""):
            kowalski = m
            break

    if not kowalski:
        errors.append("Kowalski matter not found")
    else:
        if pi_pa and kowalski.get("practiceAreaId") != pi_pa["id"]:
            errors.append(
                f"Kowalski practiceAreaId is '{kowalski.get('practiceAreaId')}', "
                f"expected '{pi_pa['id']}' (Personal Injury)"
            )

        if demand_stage_id and kowalski.get("matterStageId") != demand_stage_id:
            errors.append(
                f"Kowalski matterStageId is '{kowalski.get('matterStageId')}', "
                f"expected '{demand_stage_id}' (Demand Letter)"
            )

        billing = kowalski.get("billingPreference", {})
        if billing.get("billingMethod") != "hourly":
            errors.append(
                f"Kowalski billing method is '{billing.get('billingMethod')}', expected 'hourly'"
            )

    if errors:
        return False, "; ".join(errors)

    return True, "Workers Comp disabled, Kowalski moved to PI Demand Letter stage with hourly billing."
