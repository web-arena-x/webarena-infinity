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

    con = next((c for c in state["contacts"] if c["name"] == "Green Valley Organics"), None)
    if not con:
        return False, "Contact 'Green Valley Organics' not found."
    if inv["contactId"] != con["id"]:
        return False, "Wrong contact."
    if len(inv["lineItems"]) < 2:
        return False, f"Expected at least 2 line items, got {len(inv['lineItems'])}"
    li1 = next((l for l in inv["lineItems"] if l["description"] == "Environmental impact assessment"), None)
    if not li1:
        return False, "Line item 'Environmental impact assessment' not found."
    if li1["quantity"] != 1 or li1["unitPrice"] != 1500:
        return False, f"First line item has wrong qty/price: {li1['quantity']}x{li1['unitPrice']}"
    if li1["taxRateId"] != "tax_3":
        return False, f"First line item: expected tax_3, got {li1['taxRateId']}"
    li2 = next((l for l in inv["lineItems"] if l["description"] == "Sustainability report preparation"), None)
    if not li2:
        return False, "Line item 'Sustainability report preparation' not found."
    if li2["quantity"] != 2 or li2["unitPrice"] != 800:
        return False, f"Second line item has wrong qty/price: {li2['quantity']}x{li2['unitPrice']}"
    if li2["taxRateId"] != "tax_1":
        return False, f"Second line item: expected tax_1, got {li2['taxRateId']}"
    return True, "Draft invoice for Green Valley Organics with 2 mixed-tax line items created correctly."
