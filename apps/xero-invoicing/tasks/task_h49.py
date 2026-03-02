import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Two invoices have references starting with 'PO-':
    # INV-0042 (ref='PO-8834', status=paid) and INV-0045 (ref='PO-9012', status=awaiting_payment).
    # The one still awaiting payment is INV-0045.
    inv = None
    for i in state.get("invoices", []):
        if i.get("number") == "INV-0045":
            inv = i
            break

    if inv is None:
        return False, "Invoice INV-0045 not found."

    # Check that a $2,000 payment was added
    payments = inv.get("payments", [])
    found_payment = False
    for p in payments:
        amount = float(p.get("amount", 0))
        if abs(amount - 2000.00) < 1.00:
            found_payment = True
            break

    if not found_payment:
        payment_amounts = [p.get("amount") for p in payments]
        return False, (
            f"No $2,000 payment found on INV-0045. Payment amounts: {payment_amounts}."
        )

    # amountDue should have decreased by ~$2,000 from the original $10,890
    amount_due = float(inv.get("amountDue", 9999))
    if abs(amount_due - 8890.00) > 100.00:
        return False, (
            f"INV-0045 amountDue is ${amount_due:.2f}, expected ~$8,890 "
            f"($10,890 original - $2,000 payment)."
        )

    return True, (
        "INV-0045 (Pinnacle Construction, ref PO-9012) received a $2,000 payment. "
        "amountDue reduced to ~$8,890."
    )
