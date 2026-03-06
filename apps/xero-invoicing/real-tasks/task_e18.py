import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    invoice = next((inv for inv in state.get("invoices", []) if inv.get("number") == "INV-0060"), None)
    if invoice is None:
        return False, "Invoice INV-0060 not found."

    if invoice.get("status") != "awaiting_approval":
        return False, f"Expected invoice INV-0060 status to be 'awaiting_approval', got '{invoice.get('status')}'."

    return True, "Invoice INV-0060 (Redback Mining Supplies) has been submitted for approval successfully."
