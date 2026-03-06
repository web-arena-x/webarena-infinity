import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("invoiceSettings", {})

    tax_mode = settings.get("defaultTaxMode")
    if tax_mode != "inclusive":
        return False, f"Expected defaultTaxMode to be 'inclusive', got '{tax_mode}'."

    return True, "Default tax mode has been switched to inclusive."
