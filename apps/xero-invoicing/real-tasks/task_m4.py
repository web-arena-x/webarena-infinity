import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    invoices = state.get("invoices", [])

    # Find Atlas Engineering Consultants contact id
    contacts = state.get("contacts", [])
    atlas_id = None
    for c in contacts:
        if "atlas" in c.get("name", "").lower() and "engineering" in c.get("name", "").lower():
            atlas_id = c.get("id")
            break

    if atlas_id is None:
        return False, "Atlas Engineering Consultants contact not found in state."

    # Look for a new invoice for Atlas Engineering with matching line item
    matching_invoice = None
    for inv in invoices:
        if inv.get("contactId") != atlas_id:
            continue
        line_items = inv.get("lineItems", [])
        for li in line_items:
            qty = li.get("quantity", 0)
            price = li.get("unitPrice", 0)
            if qty == 20 and abs(price - 185.00) < 1.00:
                matching_invoice = inv
                break
        if matching_invoice:
            break

    if matching_invoice is None:
        return False, "No invoice found for Atlas Engineering Consultants with 20 hours at $185/hr."

    return True, f"New invoice {matching_invoice.get('number')} created for Atlas Engineering with 20 hours at $185/hr."
