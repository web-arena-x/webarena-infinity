import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("invoiceSettings", {})

    prefix = settings.get("invoicePrefix")
    if prefix != "TAX-":
        return False, f"Expected invoicePrefix to be 'TAX-', got '{prefix}'."

    return True, "Invoice prefix has been changed to 'TAX-' successfully."
