import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    invoice = next((inv for inv in state.get("invoices", []) if inv.get("number") == "INV-0059"), None)
    if invoice is None:
        return False, "Invoice INV-0059 not found in state (may have been fully removed)."

    if invoice.get("status") != "deleted":
        return False, f"Expected invoice INV-0059 status to be 'deleted', got '{invoice.get('status')}'."

    return True, "Invoice INV-0059 (Bright Spark Electrical) has been deleted successfully."
