import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    invoice = next((inv for inv in state.get("invoices", []) if inv.get("number") == "INV-0058"), None)
    if invoice is None:
        return False, "Invoice INV-0058 not found."

    if invoice.get("status") != "awaiting_payment":
        return False, f"Expected invoice INV-0058 status to be 'awaiting_payment', got '{invoice.get('status')}'."

    return True, "Invoice INV-0058 (Murray River Winery) has been approved successfully."
