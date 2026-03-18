import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    inv = next((i for i in state["invoices"] if i["invoiceNumber"] == "INV-0004"), None)
    if not inv:
        return False, "Invoice INV-0004 not found."
    if not inv.get("sentAt"):
        return False, "Invoice has not been marked as sent (sentAt is null)."
    has_marked = any(a["type"] == "marked_sent" for a in inv.get("activity", []))
    if not has_marked:
        return False, "No 'marked_sent' activity entry found."
    return True, "Invoice INV-0004 marked as sent successfully."
