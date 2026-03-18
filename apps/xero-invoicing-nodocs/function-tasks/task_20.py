import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    inv = next((i for i in state["invoices"] if i["invoiceNumber"] == "INV-0042"), None)
    if not inv:
        return False, "Invoice INV-0042 not found."
    expected = "Please reference invoice number on all payments."
    if inv["notes"] != expected:
        return False, f"Expected notes '{expected}', got '{inv['notes']}'"
    return True, "Invoice INV-0042 notes updated correctly."
