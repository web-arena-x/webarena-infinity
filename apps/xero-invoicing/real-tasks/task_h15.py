import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find Summit Health Group contact
    contact = next((c for c in state.get("contacts", []) if "Summit Health" in c.get("name", "")), None)
    if contact is None:
        return False, "Summit Health Group contact not found."

    contact_id = contact.get("id")

    # Find a new invoice for Summit Health (exclude existing INV-0051)
    invoices = state.get("invoices", [])
    new_invoice = next(
        (inv for inv in invoices
         if inv.get("contactId") == contact_id
         and inv.get("number") != "INV-0051"),
        None
    )

    if new_invoice is None:
        return False, "No new invoice found for Summit Health Group."

    line_items = new_invoice.get("lineItems", [])
    if len(line_items) < 2:
        return False, f"Expected at least 2 line items, found {len(line_items)}."

    # Check for annual license line: unitPrice ~1200, qty=1
    license_line = next(
        (li for li in line_items
         if abs(li.get("unitPrice", 0) - 1200.00) < 1.00
         and abs(li.get("quantity", 0) - 1) < 0.01),
        None
    )
    if license_line is None:
        return False, "No line item found with unitPrice~$1,200 and quantity=1 (annual license)."

    # Check for support line: unitPrice ~450, qty=12, discountPercent ~10
    support_line = next(
        (li for li in line_items
         if abs(li.get("unitPrice", 0) - 450.00) < 1.00
         and abs(li.get("quantity", 0) - 12) < 0.01),
        None
    )
    if support_line is None:
        return False, "No line item found with unitPrice~$450 and quantity=12 (12 months support)."

    if abs(support_line.get("discountPercent", 0) - 10) > 0.5:
        return False, f"Expected 10% discount on support line, got {support_line.get('discountPercent')}%."

    return True, f"Invoice {new_invoice.get('number')} created for Summit Health Group with annual license and 12 months support (10% discount)."
