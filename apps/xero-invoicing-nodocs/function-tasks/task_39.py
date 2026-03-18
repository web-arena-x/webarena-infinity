import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = state["settings"]
    if settings.get("invoiceNumberPrefix") != "KCL-":
        return False, f"Expected prefix 'KCL-', got '{settings.get('invoiceNumberPrefix')}'"
    return True, "Invoice number prefix changed to 'KCL-'."
