import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find Cascade Software Solutions contact
    contact = next((c for c in state.get("contacts", []) if "Cascade Software" in c.get("name", "")), None)
    if contact is None:
        return False, "Cascade Software Solutions contact not found."

    cascade_id = contact.get("id")

    # Find a new invoice that is a draft, with contactId matching Cascade, and total ~18652.70
    invoices = state.get("invoices", [])
    # Exclude existing Cascade invoice INV-0052
    new_invoice = next(
        (inv for inv in invoices
         if inv.get("contactId") == cascade_id
         and inv.get("status") == "draft"
         and abs(inv.get("total", 0) - 18652.70) < 5.00
         and inv.get("number") != "INV-0052"),
        None
    )

    if new_invoice is None:
        return False, "No new draft invoice found for Cascade Software Solutions with total ~$18,652.70."

    return True, f"Invoice {new_invoice.get('number')} copied from INV-0047, contact changed to Cascade Software, total ~$18,652.70."
