import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Record the remaining balance as a payment on partially-paid invoice INV-0034 for Pinnacle Construction Co via Business Cheque Account."""
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
        if inv.get("id") == "inv_34" or inv.get("invoiceNumber") == "INV-0034":
            target = inv
            break

    if target is None:
        return False, "Invoice INV-0034 not found in state"

    status = target.get("status")
    if status != "paid":
        return False, f"Invoice INV-0034 has status '{status}', expected 'paid'"

    amount_due = target.get("amountDue", None)
    if amount_due is None:
        return False, "Invoice INV-0034 has no amountDue field"
    if float(amount_due) > 0.01:
        return False, f"Invoice INV-0034 amountDue is {amount_due}, expected 0 (or <= 0.01)"

    # Check that a NEW payment exists for this invoice with the remaining balance (~2388.96)
    payments = state.get("payments", [])
    invoice_id = target.get("id", "inv_34")
    matching_payment = None
    for p in payments:
        if p.get("invoiceId") == invoice_id:
            amount = float(p.get("amount", 0))
            if abs(amount - 2388.96) < 0.01:
                matching_payment = p
                break

    if matching_payment is None:
        # List all payments for this invoice to help debugging
        inv_payments = [p for p in payments if p.get("invoiceId") == invoice_id]
        amounts = [p.get("amount") for p in inv_payments]
        return False, f"No payment found for invoice INV-0034 with amount ~2388.96. Found payments with amounts: {amounts}"

    bank_account_id = matching_payment.get("bankAccountId")
    if bank_account_id != "bank_1":
        return False, f"Payment bankAccountId is '{bank_account_id}', expected 'bank_1' (Business Cheque Account)"

    return True, "Invoice INV-0034 is fully paid with a new payment of ~2388.96 via Business Cheque Account"
