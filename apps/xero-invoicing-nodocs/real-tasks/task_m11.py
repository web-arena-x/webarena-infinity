import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Record a full payment for overdue invoice INV-0087 to Swift Courier Services using Business Cheque Account."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Check the invoice
    invoices = state.get("invoices", [])
    target = None
    for inv in invoices:
        if inv.get("id") == "inv_87" or inv.get("invoiceNumber") == "INV-0087":
            target = inv
            break

    if target is None:
        return False, "Invoice INV-0087 not found in state"

    status = target.get("status")
    if status != "paid":
        return False, f"Invoice INV-0087 has status '{status}', expected 'paid'"

    amount_due = target.get("amountDue", None)
    if amount_due is None:
        return False, "Invoice INV-0087 has no amountDue field"
    if float(amount_due) > 0.01:
        return False, f"Invoice INV-0087 amountDue is {amount_due}, expected 0 (or <= 0.01)"

    # Check that a payment exists for this invoice
    payments = state.get("payments", [])
    invoice_id = target.get("id", "inv_87")
    matching_payment = None
    for p in payments:
        if p.get("invoiceId") == invoice_id:
            if abs(float(p.get("amount", 0)) - 690) < 0.01:
                matching_payment = p
                break

    if matching_payment is None:
        return False, "No payment found for invoice INV-0087 with amount 690"

    bank_account_id = matching_payment.get("bankAccountId")
    if bank_account_id != "bank_1":
        return False, f"Payment bankAccountId is '{bank_account_id}', expected 'bank_1' (Business Cheque Account)"

    return True, "Invoice INV-0087 is fully paid with a payment of 690 via Business Cheque Account"
