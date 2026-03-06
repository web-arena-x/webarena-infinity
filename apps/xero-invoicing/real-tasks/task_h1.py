import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find the Pinnacle Construction quote QU-0022
    quote = next((q for q in state.get("quotes", []) if q.get("number") == "QU-0022"), None)
    if quote is None:
        return False, "Quote QU-0022 not found."

    if not quote.get("isInvoiced"):
        return False, "Quote QU-0022 has not been marked as invoiced."

    quote_contact_id = quote.get("contactId")

    # Find a new invoice with the same contactId and total matching ~52360
    invoices = state.get("invoices", [])
    matching_invoice = next(
        (inv for inv in invoices
         if inv.get("contactId") == quote_contact_id
         and abs(inv.get("total", 0) - 52360.00) < 1.00
         and inv.get("number") != "INV-0042"
         and inv.get("number") != "INV-0045"),
        None
    )

    if matching_invoice is None:
        return False, f"No new invoice found for contact '{quote_contact_id}' with total ~$52,360."

    return True, f"Invoice {matching_invoice.get('number')} created from quote QU-0022 successfully."
