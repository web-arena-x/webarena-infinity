import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Approve invoice INV-0066, then record a payment of $30,000."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    invoices = state.get("invoices", [])
    payments = state.get("payments", [])

    # Find invoice INV-0066 (inv_66)
    target = None
    for inv in invoices:
        if inv.get("id") == "inv_66" or inv.get("invoiceNumber") == "INV-0066":
            target = inv
            break

    if target is None:
        return False, "Invoice INV-0066 (inv_66) not found in state"

    errors = []
    inv_num = target.get("invoiceNumber", "INV-0066")

    # Check status - should be awaiting_payment (approved but not fully paid since 30000 < 60500)
    status = target.get("status")
    if status != "awaiting_payment":
        errors.append(f"Invoice {inv_num} has status '{status}', expected 'awaiting_payment'")

    # Check amountPaid >= 30000
    amount_paid = target.get("amountPaid", 0)
    if amount_paid < 30000 - 0.01:
        errors.append(f"Invoice {inv_num} has amountPaid={amount_paid}, expected >= 30000")

    # Check a payment exists for this invoice with amount == 30000 and bankAccountId == 'bank_1'
    matching_payment = None
    for p in payments:
        if p.get("invoiceId") == "inv_66":
            if abs(p.get("amount", 0) - 30000) < 0.01:
                matching_payment = p
                break

    if matching_payment is None:
        errors.append("No payment found for inv_66 with amount=30000")
    else:
        bank_id = matching_payment.get("bankAccountId")
        if bank_id != "bank_1":
            errors.append(f"Payment bankAccountId is '{bank_id}', expected 'bank_1'")

    if errors:
        return False, "; ".join(errors)

    return True, f"Invoice {inv_num} approved and $30,000 payment recorded via Business Cheque Account"
