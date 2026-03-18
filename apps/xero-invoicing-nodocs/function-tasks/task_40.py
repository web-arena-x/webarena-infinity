import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = state["settings"]
    if settings.get("invoiceNumberNextNumber") != 500:
        return False, f"Expected next number 500, got {settings.get('invoiceNumberNextNumber')}"
    if settings.get("invoiceNumberPadding") != 6:
        return False, f"Expected padding 6, got {settings.get('invoiceNumberPadding')}"
    return True, "Invoice number next number and padding updated correctly."
