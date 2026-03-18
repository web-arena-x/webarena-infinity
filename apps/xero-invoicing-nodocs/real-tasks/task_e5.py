import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Update the invoice number prefix to KCL- in settings."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    settings = state.get("settings", {})
    prefix = settings.get("invoiceNumberPrefix")

    if prefix == "KCL-":
        return True, "Invoice number prefix has been updated to 'KCL-'"
    else:
        return False, f"Invoice number prefix is '{prefix}', expected 'KCL-'"
