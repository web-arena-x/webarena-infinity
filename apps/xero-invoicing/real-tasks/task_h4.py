import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    invoice = next((inv for inv in state.get("invoices", []) if inv.get("number") == "INV-0056"), None)
    if invoice is None:
        return False, "Invoice INV-0056 not found."

    if invoice.get("status") != "awaiting_payment":
        return False, f"Expected INV-0056 status 'awaiting_payment', got '{invoice.get('status')}'."

    if not invoice.get("sentAt"):
        return False, "INV-0056 has not been sent (sentAt is null)."

    return True, "Invoice INV-0056 (Horizon Media) approved and sent successfully."
