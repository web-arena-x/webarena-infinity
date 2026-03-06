import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Check drug interaction alerts set to major only
    settings = state.get("settings", {})
    drug_decision_support = settings.get("drugDecisionSupport", {})
    drug_to_drug_level = drug_decision_support.get("drugToDrugLevel")

    if drug_to_drug_level != "major_only":
        return False, f"settings.drugDecisionSupport.drugToDrugLevel is '{drug_to_drug_level}', expected 'major_only'"

    return True, "Drug interaction alerts set to 'major_only' successfully"
