import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    inv = next((i for i in state["invoices"] if i["invoiceNumber"] == "INV-0034"), None)
    if not inv:
        return False, "Invoice INV-0034 not found."
    if inv["status"] != "paid":
        return False, f"Expected status 'paid', got '{inv['status']}'"
    if abs(inv["amountDue"]) > 0.01:
        return False, f"Expected amountDue ~0, got {inv['amountDue']}"
    return True, "Payment recorded on INV-0034, invoice is now paid."
