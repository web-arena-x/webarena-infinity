import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find Bright Spark Electrical contact
    contact = next((c for c in state.get("contacts", []) if "Bright Spark" in c.get("name", "")), None)
    if contact is None:
        return False, "Bright Spark Electrical contact not found."

    contact_id = contact.get("id")

    # Find a new repeating invoice for Bright Spark
    repeating_invoices = state.get("repeatingInvoices", [])
    new_ri = next(
        (ri for ri in repeating_invoices if ri.get("contactId") == contact_id),
        None
    )

    if new_ri is None:
        return False, "No repeating invoice found for Bright Spark Electrical."

    if new_ri.get("frequency") != "monthly":
        return False, f"Expected frequency 'monthly', got '{new_ri.get('frequency')}'."

    line_items = new_ri.get("lineItems", [])
    if len(line_items) == 0:
        return False, "Repeating invoice has no line items."

    return True, f"Monthly repeating invoice created for Bright Spark Electrical with {len(line_items)} line item(s)."
