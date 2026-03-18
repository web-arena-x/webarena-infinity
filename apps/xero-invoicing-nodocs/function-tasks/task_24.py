import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    inv = next((i for i in state["invoices"] if i["invoiceNumber"] == "INV-0004"), None)
    if not inv:
        return False, "Invoice INV-0004 not found."
    if inv["status"] != "awaiting_payment":
        return False, f"Expected status 'awaiting_payment', got '{inv['status']}'"
    if abs(inv["amountPaid"] - 1000) > 0.01:
        return False, f"Expected amountPaid ~1000, got {inv['amountPaid']}"
    if abs(inv["amountDue"] - 2600) > 0.01:
        return False, f"Expected amountDue ~2600, got {inv['amountDue']}"
    pay = next((p for p in state["payments"] if p["invoiceId"] == inv["id"] and abs(p["amount"] - 1000) < 0.01), None)
    if not pay:
        return False, "Payment of $1000 not found."
    return True, "Partial payment of $1000 recorded on INV-0004."
