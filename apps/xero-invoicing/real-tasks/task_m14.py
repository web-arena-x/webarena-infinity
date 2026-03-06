import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    invoices = state.get("invoices", [])
    inv = None
    for i in invoices:
        if i.get("number") == "INV-0045":
            inv = i
            break

    if inv is None:
        return False, "Invoice INV-0045 not found."

    payments = inv.get("payments", [])
    if len(payments) > 0:
        return False, f"Invoice INV-0045 still has {len(payments)} payment(s), expected none."

    amount_paid = inv.get("amountPaid", -1)
    if amount_paid != 0:
        return False, f"Invoice INV-0045 amountPaid is {amount_paid}, expected 0."

    total = inv.get("total", 0)
    amount_due = inv.get("amountDue", -1)
    if abs(amount_due - 15840.00) > 1.00:
        return False, f"Invoice INV-0045 amountDue is {amount_due}, expected 15840.00 (full total)."

    return True, "Partial payment removed from INV-0045. Payments empty, amountPaid=0, amountDue=15840."
