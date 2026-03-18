import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Record a partial payment of $2,000 against overdue invoice INV-0039 for Pacific Timber Supplies using Business Cheque Account."""
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
        if inv.get("id") == "inv_39" or inv.get("invoiceNumber") == "INV-0039":
            target = inv
            break

    if target is None:
        return False, "Invoice INV-0039 not found in state"

    errors = []

    amount_paid = target.get("amountPaid", 0)
    if amount_paid < 1999.99:
        errors.append(f"amountPaid is {amount_paid}, expected at least 2000")

    # Check that a payment exists for this invoice
    payments = state.get("payments", [])
    matching_payment = None
    for p in payments:
        if p.get("invoiceId") == "inv_39":
            if abs(p.get("amount", 0) - 2000) < 0.01:
                matching_payment = p
                break

    if matching_payment is None:
        # Also try matching by invoice number if invoiceId uses a different format
        for p in payments:
            if p.get("invoiceId") in ("inv_39", "INV-0039"):
                if abs(p.get("amount", 0) - 2000) < 0.01:
                    matching_payment = p
                    break

    if matching_payment is None:
        errors.append("No payment found for invoice inv_39/INV-0039 with amount 2000")
    else:
        bank_id = matching_payment.get("bankAccountId")
        if bank_id != "bank_1":
            errors.append(f"Payment bankAccountId is '{bank_id}', expected 'bank_1'")

    if errors:
        return False, "; ".join(errors)

    return True, "Partial payment of $2,000 recorded for INV-0039 via Business Cheque Account"
