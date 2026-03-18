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

    con = next((c for c in state["contacts"] if c["name"] == "Heritage Craft Brewery"), None)
    if not con:
        return False, "Contact 'Heritage Craft Brewery' not found."
    if inv["contactId"] != con["id"]:
        return False, "Wrong contact."
    if inv["currency"] != "AUD":
        return False, f"Expected currency AUD, got {inv['currency']}"
    li = next((l for l in inv["lineItems"] if l["description"] == "Event planning and coordination"), None)
    if not li:
        return False, "Line item 'Event planning and coordination' not found."
    if li["quantity"] != 5 or li["unitPrice"] != 300:
        return False, f"Line item has wrong qty/price: {li['quantity']}x{li['unitPrice']}"
    if li["accountCode"] != "270":
        return False, f"Expected account code '270', got '{li['accountCode']}'"
    return True, "Draft invoice for Heritage Craft Brewery in AUD created correctly."
