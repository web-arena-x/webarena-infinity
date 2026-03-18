import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    inv = next((i for i in state["invoices"] if i["invoiceNumber"] == "INV-0017"), None)
    if not inv:
        return False, "Invoice INV-0017 not found."
    if inv["status"] != "awaiting_payment":
        return False, f"Expected status 'awaiting_payment', got '{inv['status']}'"
    if not inv.get("sentAt"):
        return False, "Invoice has not been sent (sentAt is null)."
    return True, "Invoice INV-0017 approved and sent successfully."
