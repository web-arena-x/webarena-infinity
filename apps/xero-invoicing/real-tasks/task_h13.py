import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find Southern Cross Veterinary contact
    contact = next((c for c in state.get("contacts", []) if "Southern Cross" in c.get("name", "")), None)
    if contact is None:
        return False, "Southern Cross Veterinary contact not found."

    contact_id = contact.get("id")

    # Find a new repeating invoice for Southern Cross
    repeating_invoices = state.get("repeatingInvoices", [])
    new_ri = next(
        (ri for ri in repeating_invoices if ri.get("contactId") == contact_id),
        None
    )

    if new_ri is None:
        return False, "No repeating invoice found for Southern Cross Veterinary."

    if new_ri.get("frequency") != "quarterly":
        return False, f"Expected frequency 'quarterly', got '{new_ri.get('frequency')}'."

    if new_ri.get("saveAs") != "approved":
        return False, f"Expected saveAs 'approved', got '{new_ri.get('saveAs')}'."

    # Check has line item with unitPrice ~450
    line_items = new_ri.get("lineItems", [])
    matching_line = next(
        (li for li in line_items if abs(li.get("unitPrice", 0) - 450.00) < 1.00),
        None
    )
    if matching_line is None:
        return False, "No line item found with unitPrice ~$450."

    return True, f"Quarterly repeating invoice created for Southern Cross Veterinary, saved as approved, with support at $450."
