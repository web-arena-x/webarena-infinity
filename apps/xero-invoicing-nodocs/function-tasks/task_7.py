import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    inv = next((i for i in state["invoices"] if i["invoiceNumber"] == "INV-0005"), None)
    if not inv:
        return False, "Invoice INV-0005 not found."
    if inv["status"] != "awaiting_payment":
        return False, f"Expected status 'awaiting_payment', got '{inv['status']}'"
    has_approved = any(a["type"] == "approved" for a in inv.get("activity", []))
    if not has_approved:
        return False, "No 'approved' activity entry found."
    return True, "Invoice INV-0005 approved successfully."
