import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Update the notes on draft invoice INV-0093 for Apex Legal Partners to specific text."""
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
        if inv.get("id") == "inv_93" or inv.get("invoiceNumber") == "INV-0093":
            target = inv
            break

    if target is None:
        return False, "Invoice INV-0093 not found in state"

    expected_notes = "Payment due strictly within 14 days"
    notes = target.get("notes", "")

    if notes == expected_notes:
        return True, "Invoice INV-0093 notes updated to 'Payment due strictly within 14 days'"
    else:
        return False, f"Invoice INV-0093 notes is '{notes}', expected '{expected_notes}'"
