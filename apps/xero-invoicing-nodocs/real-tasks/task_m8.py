import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Approve invoice INV-0038 for Harmony Music Academy and then send it."""
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
        if inv.get("id") == "inv_38" or inv.get("invoiceNumber") == "INV-0038":
            target = inv
            break

    if target is None:
        return False, "Invoice INV-0038 not found in state"

    errors = []

    status = target.get("status")
    if status != "awaiting_payment":
        errors.append(f"Invoice status is '{status}', expected 'awaiting_payment' (approved and sent)")

    sent_at = target.get("sentAt")
    if not sent_at:
        errors.append("Invoice sentAt is empty/null, expected it to be set after sending")

    if errors:
        return False, "; ".join(errors)

    return True, "Invoice INV-0038 has been approved (status=awaiting_payment) and sent (sentAt is set)"
