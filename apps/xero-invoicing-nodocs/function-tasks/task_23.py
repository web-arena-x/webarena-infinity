import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    inv = next((i for i in state["invoices"] if i["invoiceNumber"] == "INV-0002"), None)
    if not inv:
        return False, "Invoice INV-0002 not found."
    if inv["status"] != "paid":
        return False, f"Expected status 'paid', got '{inv['status']}'"
    if abs(inv["amountPaid"] - 207) > 0.01:
        return False, f"Expected amountPaid ~207, got {inv['amountPaid']}"
    if abs(inv["amountDue"]) > 0.01:
        return False, f"Expected amountDue ~0, got {inv['amountDue']}"
    if not inv.get("paidAt"):
        return False, "paidAt is null."
    pay = next((p for p in state["payments"] if p["invoiceId"] == inv["id"] and abs(p["amount"] - 207) < 0.01), None)
    if not pay:
        return False, "Payment of $207 not found."
    return True, "Full payment of $207 recorded on INV-0002, invoice is now paid."
