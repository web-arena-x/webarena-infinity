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

    # The highest-value awaiting-payment invoice is INV-0055 ($41,800) for
    # TechVault Solutions Pty Ltd (con_002).
    # A new quote should exist for con_002, status = sent, with consulting line item.
    new_quote = None
    for q in state.get("quotes", []):
        if q.get("contactId") == "con_002" and q.get("id") not in SEED_QUOTE_IDS:
            new_quote = q
            break

    if new_quote is None:
        return False, (
            "No new quote found for TechVault Solutions (con_002). "
            "They have the highest-value awaiting-payment invoice (INV-0055, $41,800)."
        )

    if new_quote.get("status") != "sent":
        return False, (
            f"New quote '{new_quote.get('number')}' status is '{new_quote.get('status')}', "
            f"expected 'sent'."
        )

    line_items = new_quote.get("lineItems", [])
    found = False
    for li in line_items:
        price = float(li.get("unitPrice", 0))
        qty = li.get("quantity", 0)
        if abs(price - 250.00) < 10.00 and qty == 10:
            found = True
            break

    if not found:
        items = [(li.get("unitPrice"), li.get("quantity")) for li in line_items]
        return False, (
            f"No line item with qty 10 and unitPrice ~$250 (consulting) found. Items: {items}."
        )

    return True, (
        f"Quote '{new_quote.get('number')}' sent to TechVault Solutions "
        f"(highest awaiting-payment invoice) for 10 hours consulting at $250/hr."
    )
