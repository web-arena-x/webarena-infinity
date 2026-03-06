import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    invoice = next((inv for inv in state.get("invoices", []) if inv.get("number") == "INV-0054"), None)
    if invoice is None:
        return False, "Invoice INV-0054 not found."

    if invoice.get("status") != "voided":
        return False, f"Expected invoice INV-0054 status to be 'voided', got '{invoice.get('status')}'."

    if invoice.get("amountDue", -1) != 0:
        return False, f"Expected invoice INV-0054 amountDue to be 0, got {invoice.get('amountDue')}."

    return True, "Invoice INV-0054 (Sapphire Bay Resort) has been voided successfully."
