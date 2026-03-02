import requests


# Seed quote IDs
SEED_QUOTE_IDS = {
    "quo_001", "quo_002", "quo_003", "quo_004",
    "quo_005", "quo_006", "quo_007", "quo_008",
}


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Metro Fabrication Works = con_019
    new_quote = None
    for q in state.get("quotes", []):
        if q.get("contactId") == "con_019" and q.get("id") not in SEED_QUOTE_IDS:
            new_quote = q
            break

    if new_quote is None:
        return False, "No new quote found for Metro Fabrication Works (con_019)."

    if new_quote.get("status") != "sent":
        return False, (
            f"New quote '{new_quote.get('number')}' status is '{new_quote.get('status')}', "
            f"expected 'sent'."
        )

    line_items = new_quote.get("lineItems", [])
    if len(line_items) < 2:
        return False, f"New quote has {len(line_items)} line item(s), expected at least 2."

    found_setup = False
    found_cables = False
    for li in line_items:
        price = float(li.get("unitPrice", 0))
        qty = li.get("quantity", 0)
        if abs(price - 500.00) < 10.00:
            found_setup = True
        if abs(price - 12.50) < 2.00 and qty == 20:
            found_cables = True

    if not found_setup:
        prices = [li.get("unitPrice") for li in line_items]
        return False, f"No line item with unitPrice ~$500 (setup fee) found. Prices: {prices}."

    if not found_cables:
        items = [(li.get("unitPrice"), li.get("quantity")) for li in line_items]
        return False, f"No line item with unitPrice ~$12.50 and qty 20 (USB-C cables) found. Items: {items}."

    return True, (
        f"Quote '{new_quote.get('number')}' created and sent for Metro Fabrication Works "
        f"with setup fee ($500) and 20 USB-C cables ($12.50 each)."
    )
