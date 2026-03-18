import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Void invoice INV-0068 for Apex Legal Partners."""
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
        if inv.get("invoiceNumber") == "INV-0068":
            target = inv
            break

    if target is None:
        return False, "Invoice INV-0068 not found in state"

    status = target.get("status")
    if status != "voided":
        return False, f"Invoice INV-0068 has status '{status}', expected 'voided'"

    voided_at = target.get("voidedAt")
    if voided_at is None:
        return False, "Invoice INV-0068 has voidedAt = None, expected it to be set after voiding"

    return True, "Invoice INV-0068 has been voided (status='voided', voidedAt is set)"
