import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})
    drug_support = settings.get("drugDecisionSupport", {})
    level = drug_support.get("drugToDrugLevel")

    expected = "major_only"
    if level != expected:
        return False, f"drugToDrugLevel is '{level}', expected '{expected}'."

    return True, f"drugToDrugLevel successfully changed to '{expected}'."
