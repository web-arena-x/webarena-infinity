import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = state["settings"]
    if settings.get("defaultTaxRateId") != "tax_3":
        return False, f"Expected defaultTaxRateId 'tax_3', got '{settings.get('defaultTaxRateId')}'"
    return True, "Default tax rate changed to No GST (0%)."
