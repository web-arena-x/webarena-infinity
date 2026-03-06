import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    invoices = state.get("invoices", [])
    inv = None
    for i in invoices:
        if i.get("number") == "INV-0053":
            inv = i
            break

    if inv is None:
        return False, "Invoice INV-0053 not found."

    if inv.get("status") != "paid":
        return False, f"Invoice INV-0053 status is '{inv.get('status')}', expected 'paid'."

    amount_due = inv.get("amountDue", -1)
    if amount_due != 0:
        return False, f"Invoice INV-0053 amountDue is {amount_due}, expected 0."

    payments = inv.get("payments", [])
    if not payments:
        return False, "Invoice INV-0053 has no payments recorded."

    found_payment = False
    for p in payments:
        if abs(p.get("amount", 0) - 823.90) < 0.10:
            found_payment = True
            break

    if not found_payment:
        return False, f"No payment of approximately $823.90 found on INV-0053. Payments: {payments}"

    return True, "Invoice INV-0053 is fully paid with payment of $823.90."
