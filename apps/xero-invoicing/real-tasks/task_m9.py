import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find Sapphire Bay Resort contact
    contacts = state.get("contacts", [])
    sapphire_id = None
    for c in contacts:
        if "sapphire" in c.get("name", "").lower() and "bay" in c.get("name", "").lower():
            sapphire_id = c.get("id")
            break

    if sapphire_id is None:
        return False, "Sapphire Bay Resort contact not found in state."

    quotes = state.get("quotes", [])
    matching_quote = None
    for q in quotes:
        if q.get("contactId") != sapphire_id:
            continue
        line_items = q.get("lineItems", [])
        for li in line_items:
            qty = li.get("quantity", 0)
            price = li.get("unitPrice", 0)
            if qty == 5 and abs(price - 2200.00) < 1.00:
                matching_quote = q
                break
        if matching_quote:
            break

    if matching_quote is None:
        return False, "No quote found for Sapphire Bay Resort with 5 days at $2,200/day."

    return True, f"New quote {matching_quote.get('number')} created for Sapphire Bay Resort with 5 days training at $2,200/day."
