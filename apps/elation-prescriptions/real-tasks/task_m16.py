import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    settings = state.get("settings", {})

    # Check drugDecisionSupport.drugToDrugLevel == "major_moderate"
    drug_support = settings.get("drugDecisionSupport", {})
    drug_level = drug_support.get("drugToDrugLevel", "")
    if drug_level != "major_moderate":
        return False, f"drugDecisionSupport.drugToDrugLevel is '{drug_level}', expected 'major_moderate'"

    # Check showCostEstimates is False
    show_cost = settings.get("showCostEstimates")
    if show_cost is not False:
        return False, f"settings.showCostEstimates is {show_cost}, expected false"

    return True, "Drug interaction level set to Major and Moderate only, cost estimates disabled"
