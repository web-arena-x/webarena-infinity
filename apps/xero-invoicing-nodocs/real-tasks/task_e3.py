import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Delete the draft invoice INV-0054 for Nexus Technologies."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    invoices = state.get("invoices", [])

    for inv in invoices:
        if inv.get("invoiceNumber") == "INV-0054":
            return False, f"Invoice INV-0054 still exists in state with status '{inv.get('status')}'"

    return True, "Invoice INV-0054 has been successfully deleted"
