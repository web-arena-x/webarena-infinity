import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    inv = next((i for i in state["invoices"] if i["invoiceNumber"] == "INV-0005"), None)
    if not inv:
        return False, "Invoice INV-0005 not found."
    if inv["reference"] != "UPDATED-REF-001":
        return False, f"Expected reference 'UPDATED-REF-001', got '{inv['reference']}'"
    return True, "Invoice INV-0005 reference updated correctly."
