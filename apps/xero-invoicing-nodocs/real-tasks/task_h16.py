import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Create a new draft invoice for CloudBridge Software in AUD with 2 line items."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    invoices = state.get("invoices", [])

    # Find a NEW draft invoice for con_21 (CloudBridge Software)
    new_inv = None
    for inv in invoices:
        if inv.get("contactId") == "con_21" and inv.get("status") == "draft":
            new_inv = inv
            break

    if new_inv is None:
        return False, "No new draft invoice found for CloudBridge Software (con_21)"

    errors = []
    inv_num = new_inv.get("invoiceNumber", new_inv.get("id"))

    # Check currency
    currency = new_inv.get("currency", new_inv.get("currencyCode"))
    if currency != "AUD":
        errors.append(f"Invoice {inv_num} has currency '{currency}', expected 'AUD'")

    # Check reference
    ref = new_inv.get("reference")
    if ref != "CB-INT-001":
        errors.append(f"Invoice {inv_num} has reference '{ref}', expected 'CB-INT-001'")

    # Check dates
    issue_date = new_inv.get("issueDate")
    if issue_date != "2026-03-18":
        errors.append(f"Invoice {inv_num} has issueDate '{issue_date}', expected '2026-03-18'")

    due_date = new_inv.get("dueDate")
    if due_date != "2026-04-17":
        errors.append(f"Invoice {inv_num} has dueDate '{due_date}', expected '2026-04-17'")

    # Check line items
    line_items = new_inv.get("lineItems", [])
    if len(line_items) != 2:
        errors.append(f"Invoice {inv_num} has {len(line_items)} line items, expected 2")
    else:
        found_api = False
        found_docs = False

        for li in line_items:
            desc = (li.get("description") or "").lower().strip()
            qty = li.get("quantity", 0)
            price = li.get("unitPrice", li.get("unitAmount", 0))

            if "api" in desc and "integrat" in desc:
                found_api = True
                if abs(qty - 60) > 0.01:
                    errors.append(f"API integration line item has quantity {qty}, expected 60")
                if abs(price - 175) > 0.01:
                    errors.append(f"API integration line item has unitPrice {price}, expected 175")
            elif "technical" in desc and "document" in desc:
                found_docs = True
                if abs(qty - 20) > 0.01:
                    errors.append(f"Technical documentation line item has quantity {qty}, expected 20")
                if abs(price - 120) > 0.01:
                    errors.append(f"Technical documentation line item has unitPrice {price}, expected 120")

        if not found_api:
            errors.append("Missing line item for 'API integration'")
        if not found_docs:
            errors.append("Missing line item for 'Technical documentation'")

    if errors:
        return False, "; ".join(errors)

    return True, f"New draft invoice {inv_num} for CloudBridge Software created in AUD with correct line items"
