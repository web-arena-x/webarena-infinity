import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    original_ids = {f"inv_{i}" for i in range(1, 114)}
    new_invs = [i for i in state["invoices"] if i["id"] not in original_ids]
    if not new_invs:
        return False, "No new invoice found."
    inv = new_invs[0]

    con = next((c for c in state["contacts"] if c["name"] == "DataFlow Analytics Inc"), None)
    if not con:
        return False, "Contact 'DataFlow Analytics Inc' not found."
    if inv["contactId"] != con["id"]:
        return False, "Wrong contact."
    if inv["currency"] != "USD":
        return False, f"Expected currency USD, got {inv['currency']}"
    if inv["status"] != "draft":
        return False, f"Expected status 'draft', got '{inv['status']}'"
    li = next((l for l in inv["lineItems"] if l["description"] == "Cloud migration assessment"), None)
    if not li:
        return False, "Line item 'Cloud migration assessment' not found."
    if li["quantity"] != 1:
        return False, f"Expected quantity 1, got {li['quantity']}"
    if li["unitPrice"] != 2500:
        return False, f"Expected unit price 2500, got {li['unitPrice']}"
    return True, "Draft invoice for DataFlow Analytics Inc in USD created correctly."
