import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find Northern Territory Power Corp contact
    contact = next((c for c in state.get("contacts", []) if "Northern Territory" in c.get("name", "")), None)
    if contact is None:
        return False, "Northern Territory Power Corp contact not found."

    contact_id = contact.get("id")

    # Find a new quote for NT Power (exclude any existing quotes)
    quotes = state.get("quotes", [])
    new_quote = next(
        (q for q in quotes if q.get("contactId") == contact_id),
        None
    )

    if new_quote is None:
        return False, "No quote found for Northern Territory Power Corp."

    # Check at least 2 line items
    line_items = new_quote.get("lineItems", [])
    if len(line_items) < 2:
        return False, f"Expected at least 2 line items, found {len(line_items)}."

    # Check status is sent
    if new_quote.get("status") != "sent":
        return False, f"Expected quote status 'sent', got '{new_quote.get('status')}'."

    # Check sentAt is not None
    if not new_quote.get("sentAt"):
        return False, "Quote has not been sent (sentAt is null)."

    return True, f"Quote {new_quote.get('number')} created for NT Power Corp with {len(line_items)} line items and sent."
