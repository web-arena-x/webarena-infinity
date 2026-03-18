import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    inv = next((i for i in state["invoices"] if i["invoiceNumber"] == "INV-0108"), None)
    if inv:
        return False, "Invoice INV-0108 still exists (should have been deleted)."
    if len(state["invoices"]) != 112:
        return False, f"Expected 112 invoices, got {len(state['invoices'])}"
    return True, "Invoice INV-0108 deleted successfully."
