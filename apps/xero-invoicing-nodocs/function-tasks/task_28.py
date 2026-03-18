import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    inv = next((i for i in state["invoices"] if i["invoiceNumber"] == "INV-0006"), None)
    if not inv:
        return False, "Invoice INV-0006 not found."
    inv_payments = [p for p in state["payments"] if p["invoiceId"] == inv["id"]]
    if len(inv_payments) != 0:
        return False, f"Expected 0 payments for INV-0006, found {len(inv_payments)}"
    if abs(inv["amountPaid"]) > 0.01:
        return False, f"Expected amountPaid ~0, got {inv['amountPaid']}"
    if abs(inv["amountDue"] - 14950) > 0.01:
        return False, f"Expected amountDue ~14950, got {inv['amountDue']}"
    return True, "Partial payment removed from INV-0006 correctly."
