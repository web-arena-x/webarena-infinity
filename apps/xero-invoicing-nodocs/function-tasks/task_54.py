import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    inv = next((i for i in state["invoices"] if i["invoiceNumber"] == "INV-0001"), None)
    if not inv:
        return False, "Invoice INV-0001 not found."
    if inv["status"] != "awaiting_payment":
        return False, f"Expected status 'awaiting_payment' (reverted), got '{inv['status']}'"
    if abs(inv["amountPaid"]) > 0.01:
        return False, f"Expected amountPaid ~0, got {inv['amountPaid']}"
    if inv.get("paidAt") is not None:
        return False, "paidAt should be null after payment removal."
    inv_payments = [p for p in state["payments"] if p["invoiceId"] == inv["id"]]
    if len(inv_payments) != 0:
        return False, f"Expected 0 payments for INV-0001, found {len(inv_payments)}"
    return True, "Payment removed from INV-0001, status reverted to awaiting_payment."
