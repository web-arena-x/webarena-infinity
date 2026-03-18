import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    inv5 = next((i for i in state["invoices"] if i["invoiceNumber"] == "INV-0005"), None)
    if not inv5:
        return False, "Invoice INV-0005 not found."
    if inv5["status"] != "awaiting_payment":
        return False, f"INV-0005: expected 'awaiting_payment', got '{inv5['status']}'"
    inv54 = next((i for i in state["invoices"] if i["invoiceNumber"] == "INV-0054"), None)
    if not inv54:
        return False, "Invoice INV-0054 not found."
    if inv54["status"] != "awaiting_payment":
        return False, f"INV-0054: expected 'awaiting_payment', got '{inv54['status']}'"
    return True, "Invoices INV-0005 and INV-0054 bulk approved successfully."
