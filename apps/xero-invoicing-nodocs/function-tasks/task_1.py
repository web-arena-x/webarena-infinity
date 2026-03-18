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

    con = next((c for c in state["contacts"] if c["name"] == "Ridgeway University"), None)
    if not con:
        return False, "Contact 'Ridgeway University' not found."
    if inv["contactId"] != con["id"]:
        return False, f"Wrong contact: expected {con['id']}, got {inv['contactId']}"
    if inv["status"] != "draft":
        return False, f"Expected status 'draft', got '{inv['status']}'"
    li = next((l for l in inv["lineItems"] if l["description"] == "Strategic consulting session"), None)
    if not li:
        return False, "Line item 'Strategic consulting session' not found."
    if li["quantity"] != 3:
        return False, f"Expected quantity 3, got {li['quantity']}"
    if li["unitPrice"] != 450:
        return False, f"Expected unit price 450, got {li['unitPrice']}"
    return True, "Draft invoice for Ridgeway University created correctly."
