import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    inv = next((i for i in state["invoices"] if i["invoiceNumber"] == "INV-0042"), None)
    if not inv:
        return False, "Invoice INV-0042 not found."
    if inv["status"] != "awaiting_payment":
        return False, f"Expected status 'awaiting_payment', got '{inv['status']}'"
    if not inv.get("sentAt"):
        return False, "Invoice has not been sent (sentAt is null)."
    has_sent = any(a["type"] == "sent" for a in inv.get("activity", []))
    if not has_sent:
        return False, "No 'sent' activity entry found."
    return True, "Invoice INV-0042 approved and sent successfully."
