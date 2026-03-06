import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("invoiceSettings", {})

    if settings.get("showItemCode") is not False:
        return False, f"Expected showItemCode to be False, got {settings.get('showItemCode')}."

    return True, "Item code column has been hidden successfully."
