import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Check drug-to-allergy alerts are disabled
    settings = state.get("settings", {})
    drug_decision_support = settings.get("drugDecisionSupport", {})
    drug_to_allergy_enabled = drug_decision_support.get("drugToAllergyEnabled")

    if drug_to_allergy_enabled is not False:
        return False, f"settings.drugDecisionSupport.drugToAllergyEnabled is {drug_to_allergy_enabled}, expected false"

    return True, "Drug-to-allergy alerts disabled successfully"
