import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Update the reference on draft invoice INV-0042 for Clearwater Environmental to WO-55555."""
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
        if inv.get("id") == "inv_42" or inv.get("invoiceNumber") == "INV-0042":
            target = inv
            break

    if target is None:
        return False, "Invoice INV-0042 not found in state"

    reference = target.get("reference", "")
    if reference is None:
        reference = ""

    if reference.strip() == "WO-55555":
        return True, "Invoice INV-0042 reference updated to 'WO-55555'"
    else:
        return False, f"Invoice INV-0042 reference is '{reference}', expected 'WO-55555'"
