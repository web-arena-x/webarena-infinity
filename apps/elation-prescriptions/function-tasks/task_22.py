import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})
    drug_support = settings.get("drugDecisionSupport", {})
    enabled = drug_support.get("drugToAllergyEnabled")

    if enabled is not False:
        return False, f"drugToAllergyEnabled is {enabled}, expected false."

    return True, "drugToAllergyEnabled successfully set to false."
