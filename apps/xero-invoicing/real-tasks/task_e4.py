import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    invoice = next((inv for inv in state.get("invoices", []) if inv.get("number") == "INV-0057"), None)
    if invoice is None:
        return False, "Invoice INV-0057 not found."

    if invoice.get("status") != "awaiting_payment":
        return False, f"Expected invoice INV-0057 status to be 'awaiting_payment', got '{invoice.get('status')}'."

    if not invoice.get("sentAt"):
        return False, "Expected invoice INV-0057 sentAt to be set (not None/empty), but it is not."

    return True, "Invoice INV-0057 (Stellar Education Services) has been marked as sent successfully."
