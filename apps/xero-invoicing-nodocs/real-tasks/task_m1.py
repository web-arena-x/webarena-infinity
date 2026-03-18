import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Record a full payment for invoice INV-0007 to Green Valley Organics using the Business Cheque Account."""
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
        if inv.get("id") == "inv_7" or inv.get("invoiceNumber") == "INV-0007":
            target = inv
            break

    if target is None:
        return False, "Invoice INV-0007 not found in state"

    errors = []

    status = target.get("status")
    if status != "paid":
        errors.append(f"Invoice status is '{status}', expected 'paid'")

    total = target.get("total", 0)
    amount_paid = target.get("amountPaid", 0)
    amount_due = target.get("amountDue")

    if abs(amount_paid - 5330.25) > 0.01 and abs(amount_paid - total) > 0.01:
        errors.append(f"amountPaid is {amount_paid}, expected {total} (5330.25)")

    if amount_due is not None and abs(amount_due) > 0.01:
        errors.append(f"amountDue is {amount_due}, expected 0")

    # Check that a payment exists for this invoice
    payments = state.get("payments", [])
    matching_payment = None
    for p in payments:
        if p.get("invoiceId") == "inv_7":
            if abs(p.get("amount", 0) - 5330.25) < 0.01:
                matching_payment = p
                break

    if matching_payment is None:
        errors.append("No payment found for invoice inv_7 with amount 5330.25")
    else:
        bank_id = matching_payment.get("bankAccountId")
        if bank_id != "bank_1":
            errors.append(f"Payment bankAccountId is '{bank_id}', expected 'bank_1'")

    if errors:
        return False, "; ".join(errors)

    return True, "Invoice INV-0007 is fully paid with correct payment recorded via Business Cheque Account"
