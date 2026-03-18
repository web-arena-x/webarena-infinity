import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Approve invoice INV-0008 for Metro Print Solutions."""
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
        if inv.get("invoiceNumber") == "INV-0008":
            target = inv
            break

    if target is None:
        return False, "Invoice INV-0008 not found in state"

    status = target.get("status")
    if status == "awaiting_payment":
        return True, "Invoice INV-0008 has been approved and is now awaiting payment"
    else:
        return False, f"Invoice INV-0008 has status '{status}', expected 'awaiting_payment'"
