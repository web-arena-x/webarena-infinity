import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Update the currency on draft invoice INV-0020 for Heritage Craft Brewery to NZD."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    invoices = state.get("invoices", [])
    target = None
    for inv in invoices:
        if inv.get("id") == "inv_20" or inv.get("invoiceNumber") == "INV-0020":
            target = inv
            break

    if target is None:
        return False, "Invoice INV-0020 not found in state"

    currency = target.get("currency")
    if currency == "NZD":
        return True, "Invoice INV-0020 currency has been updated to NZD"
    else:
        return False, f"Invoice INV-0020 currency is '{currency}', expected 'NZD'"
