import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find TechVault Solutions contact
    contact = next((c for c in state.get("contacts", []) if "TechVault" in c.get("name", "")), None)
    if contact is None:
        return False, "TechVault Solutions contact not found."

    contact_id = contact.get("id")

    # Find a new credit note for TechVault (exclude existing CN-0010)
    credit_notes = state.get("creditNotes", [])
    new_cn = next(
        (cn for cn in credit_notes
         if cn.get("contactId") == contact_id
         and cn.get("number") != "CN-0010"),
        None
    )

    if new_cn is None:
        return False, "No new credit note found for TechVault Solutions."

    # Check line item: qty=5, unitPrice ~185
    line_items = new_cn.get("lineItems", [])
    matching_line = next(
        (li for li in line_items
         if abs(li.get("quantity", 0) - 5) < 0.01
         and abs(li.get("unitPrice", 0) - 185.00) < 1.00),
        None
    )
    if matching_line is None:
        return False, "No line item found with quantity=5 and unitPrice~$185."

    # Check status is awaiting_payment (approved)
    if new_cn.get("status") != "awaiting_payment":
        return False, f"Expected credit note status 'awaiting_payment', got '{new_cn.get('status')}'."

    return True, f"Credit note {new_cn.get('number')} created for TechVault Solutions (5 hrs @ $185), approved."
