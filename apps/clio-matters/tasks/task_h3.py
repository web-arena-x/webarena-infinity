import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Find Personal Injury practice area
    practice_areas = state.get("practiceAreas", [])
    pi_pa = next(
        (pa for pa in practice_areas if pa.get("id") == "pa_1" or "personal injury" in pa.get("name", "").lower()),
        None
    )

    if pi_pa is None:
        return False, "Could not find Personal Injury practice area."

    pi_pa_id = pi_pa["id"]

    # Find all PI matters and determine which has the highest budget
    pi_matters = [
        m for m in state.get("matters", [])
        if m.get("practiceAreaId") == pi_pa_id
    ]

    if not pi_matters:
        return False, "No Personal Injury matters found."

    # Find the matter with the highest budget
    highest_budget_matter = None
    highest_budget = -1

    for m in pi_matters:
        billing = m.get("billing", {})
        budget = billing.get("budget")
        if budget is not None:
            try:
                budget_val = float(budget)
                if budget_val > highest_budget:
                    highest_budget = budget_val
                    highest_budget_matter = m
            except (ValueError, TypeError):
                continue

    if highest_budget_matter is None:
        return False, "No PI matter found with a budget set."

    matter_id = highest_budget_matter.get("id")
    description = highest_budget_matter.get("description", "")
    attorney_id = highest_budget_matter.get("responsibleAttorneyId")

    if attorney_id != "user_3":
        return False, (
            f"PI matter with highest budget ({matter_id}: '{description}', "
            f"budget=${highest_budget:,.0f}) has responsibleAttorneyId '{attorney_id}', "
            f"expected 'user_3' (Diana Reyes)."
        )

    return True, (
        f"PI matter with highest budget ({matter_id}: '{description}', "
        f"budget=${highest_budget:,.0f}) has Diana Reyes (user_3) as responsible attorney."
    )
