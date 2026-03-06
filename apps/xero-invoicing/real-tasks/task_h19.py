import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    invoice = next((inv for inv in state.get("invoices", []) if inv.get("number") == "INV-0060"), None)
    if invoice is None:
        return False, "Invoice INV-0060 not found."

    # Should be awaiting_payment (approved + partial payment)
    if invoice.get("status") != "awaiting_payment":
        return False, f"Expected INV-0060 status 'awaiting_payment', got '{invoice.get('status')}'."

    # Check has payment ~$1,000
    payments = invoice.get("payments", [])
    payment_1k = next((p for p in payments if abs(p.get("amount", 0) - 1000.00) < 1.00), None)
    if payment_1k is None:
        return False, "No payment of ~$1,000 found on INV-0060."

    # Check amountDue ~2450 (3450 - 1000)
    expected_due = 3450.00 - 1000.00
    if abs(invoice.get("amountDue", 0) - expected_due) > 1.00:
        return False, f"Expected amountDue ~${expected_due:.2f}, got ${invoice.get('amountDue', 0)}."

    return True, "INV-0060 (Redback Mining) approved with $1,000 partial payment, amountDue ~$2,450."
