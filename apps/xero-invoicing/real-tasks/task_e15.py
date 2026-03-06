import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("invoiceSettings", {})

    if settings.get("showDiscountColumn") is not False:
        return False, f"Expected showDiscountColumn to be False, got {settings.get('showDiscountColumn')}."

    return True, "Discount column has been hidden successfully."
