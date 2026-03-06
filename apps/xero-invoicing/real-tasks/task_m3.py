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

    if inv.get("status") != "paid":
        return False, f"Invoice INV-0045 status is '{inv.get('status')}', expected 'paid'."

    amount_due = inv.get("amountDue", -1)
    if amount_due != 0:
        return False, f"Invoice INV-0045 amountDue is {amount_due}, expected 0."

    return True, "Invoice INV-0045 (Pinnacle Construction) is fully paid with amountDue=0."
