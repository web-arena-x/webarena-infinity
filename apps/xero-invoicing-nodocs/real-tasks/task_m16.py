import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Change the invoice number padding to 5 digits and the prefix to KINV- in settings."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    settings = state.get("settings", {})
    if not settings:
        return False, "No settings found in state"

    errors = []

    padding = settings.get("invoiceNumberPadding")
    if padding != 5:
        # Also accept string "5"
        if str(padding) == "5":
            pass
        else:
            errors.append(f"invoiceNumberPadding is {padding!r}, expected 5")

    prefix = settings.get("invoiceNumberPrefix")
    if prefix != "KINV-":
        errors.append(f"invoiceNumberPrefix is '{prefix}', expected 'KINV-'")

    if errors:
        return False, "; ".join(errors)

    return True, "Settings updated: invoice number padding is 5 and prefix is 'KINV-'"
