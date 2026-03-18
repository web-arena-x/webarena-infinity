import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    inv = next((i for i in state["invoices"] if i["invoiceNumber"] == "INV-0015"), None)
    if not inv:
        return False, "Invoice INV-0015 not found."
    if abs(inv["amountPaid"] - 10000) > 0.01:
        return False, f"Expected amountPaid ~10000, got {inv['amountPaid']}"
    expected_due = 35937.5 - 10000
    if abs(inv["amountDue"] - expected_due) > 0.01:
        return False, f"Expected amountDue ~{expected_due}, got {inv['amountDue']}"
    pay = next((p for p in state["payments"] if p["invoiceId"] == inv["id"] and abs(p["amount"] - 10000) < 0.01), None)
    if not pay:
        return False, "Payment of $10000 not found."
    return True, "Payment of $10000 recorded on overdue invoice INV-0015."
