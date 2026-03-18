import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Send invoice INV-0017 to Clearwater Environmental."""
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
        if inv.get("invoiceNumber") == "INV-0017":
            target = inv
            break

    if target is None:
        return False, "Invoice INV-0017 not found in state"

    status = target.get("status")
    if status != "awaiting_payment":
        return False, f"Invoice INV-0017 has status '{status}', expected 'awaiting_payment'"

    sent_at = target.get("sentAt")
    if sent_at is None:
        return False, "Invoice INV-0017 has sentAt = None, expected it to be set after sending"

    return True, "Invoice INV-0017 has been sent (status='awaiting_payment', sentAt is set)"
