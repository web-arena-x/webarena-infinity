import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find Wellington & Partners contact
    contact = next((c for c in state.get("contacts", []) if "Wellington" in c.get("name", "")), None)
    if contact is None:
        return False, "Wellington & Partners contact not found."

    contact_id = contact.get("id")

    # Find a new invoice for Wellington in NZD
    invoices = state.get("invoices", [])
    # Exclude known existing invoices for Wellington (INV-0066)
    new_invoice = next(
        (inv for inv in invoices
         if inv.get("contactId") == contact_id
         and inv.get("currency") == "NZD"
         and inv.get("number") != "INV-0066"),
        None
    )

    if new_invoice is None:
        return False, "No new NZD invoice found for Wellington & Partners."

    # Check line item: qty=16, unitPrice ~250
    line_items = new_invoice.get("lineItems", [])
    consulting_line = next(
        (li for li in line_items
         if abs(li.get("quantity", 0) - 16) < 0.01
         and abs(li.get("unitPrice", 0) - 250.00) < 1.00),
        None
    )
    if consulting_line is None:
        return False, "No line item found with quantity=16 and unitPrice~$250."

    # Check status is awaiting_payment (sent invoice)
    if new_invoice.get("status") != "awaiting_payment":
        return False, f"Expected invoice status 'awaiting_payment', got '{new_invoice.get('status')}'."

    # Check sentAt is not None
    if not new_invoice.get("sentAt"):
        return False, "Invoice has not been sent (sentAt is null)."

    return True, f"Invoice {new_invoice.get('number')} created for Wellington & Partners in NZD with 16 hours consulting, and sent."
