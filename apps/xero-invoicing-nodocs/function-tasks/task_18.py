import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    inv = next((i for i in state["invoices"] if i["invoiceNumber"] == "INV-0083"), None)
    if not inv:
        return False, "Invoice INV-0083 not found."
    if len(inv["lineItems"]) < 4:
        return False, f"Expected at least 4 line items, got {len(inv['lineItems'])}"
    li = next((l for l in inv["lineItems"] if l["description"] == "Technical documentation"), None)
    if not li:
        return False, "Line item 'Technical documentation' not found."
    if li["quantity"] != 4:
        return False, f"Expected quantity 4, got {li['quantity']}"
    if li["unitPrice"] != 125:
        return False, f"Expected unit price 125, got {li['unitPrice']}"
    return True, "Line item 'Technical documentation' added to INV-0083 correctly."
