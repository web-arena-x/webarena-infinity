import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # INV-0046 (Baxter & Associates Legal) has the earliest due date (2026-02-01)
    # among all overdue invoices (due before 2026-03-02 and status awaiting_payment).
    inv = None
    for i in state.get("invoices", []):
        if i.get("number") == "INV-0046":
            inv = i
            break

    if inv is None:
        return False, "Invoice INV-0046 not found."

    status = inv.get("status", "")
    if status != "paid":
        return False, f"INV-0046 status is '{status}', expected 'paid'."

    amount_due = float(inv.get("amountDue", 9999))
    if amount_due > 1.00:
        return False, f"INV-0046 amountDue is ${amount_due:.2f}, expected ~$0."

    return True, "Overdue invoice INV-0046 (Baxter & Associates Legal, due 2026-02-01) fully paid."
