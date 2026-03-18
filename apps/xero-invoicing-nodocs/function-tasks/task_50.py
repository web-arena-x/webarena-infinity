import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    inv39 = next((i for i in state["invoices"] if i["invoiceNumber"] == "INV-0039"), None)
    if not inv39:
        return False, "Invoice INV-0039 not found."
    target_contact_id = inv39["contactId"]

    original_ids = {f"inv_{i}" for i in range(1, 114)}
    new_invs = [i for i in state["invoices"] if i["id"] not in original_ids]
    if not new_invs:
        return False, "No new invoice found."
    inv = new_invs[0]
    if inv["contactId"] != target_contact_id:
        return False, f"Expected contact {target_contact_id}, got {inv['contactId']}"
    if inv["status"] != "draft":
        return False, f"Expected status 'draft', got '{inv['status']}'"
    li = next((l for l in inv["lineItems"] if l["description"] == "Follow-up audit"), None)
    if not li:
        return False, "Line item 'Follow-up audit' not found."
    if li["quantity"] != 1:
        return False, f"Expected quantity 1, got {li['quantity']}"
    if li["unitPrice"] != 750:
        return False, f"Expected unit price 750, got {li['unitPrice']}"
    return True, "Draft invoice for contact of INV-0039 created correctly."
