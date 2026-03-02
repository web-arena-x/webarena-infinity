import requests


SEED_QUOTE_IDS = {"quo_001", "quo_002", "quo_003", "quo_004", "quo_005", "quo_006", "quo_007", "quo_008"}


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # QU-0028 (Metro Fabrication Works, sent) should be declined
    old_quo = None
    for q in state.get("quotes", []):
        if q.get("number") == "QU-0028":
            old_quo = q
            break

    if old_quo is None:
        return False, "Quote QU-0028 not found."

    if old_quo.get("status") != "declined":
        return False, (
            f"QU-0028 status is '{old_quo.get('status')}', expected 'declined'."
        )

    # A new quote should exist for Metro Fabrication Works (con_019)
    new_quo = None
    for q in state.get("quotes", []):
        if q.get("contactId") == "con_019" and q.get("id") not in SEED_QUOTE_IDS:
            new_quo = q
            break

    if new_quo is None:
        return False, "No new quote found for Metro Fabrication Works (con_019)."

    if new_quo.get("status") != "sent":
        return False, (
            f"New quote '{new_quo.get('number')}' status is '{new_quo.get('status')}', "
            f"expected 'sent'."
        )

    if not new_quo.get("sentAt"):
        return False, f"New quote '{new_quo.get('number')}' has not been sent."

    # Check line item: 5 Widget B at ~$49.95
    line_items = new_quo.get("lineItems", [])
    found = False
    for li in line_items:
        price = float(li.get("unitPrice", 0))
        qty = li.get("quantity", 0)
        if abs(price - 49.95) < 5.00 and qty == 5:
            found = True
            break

    if not found:
        items = [(li.get("unitPrice"), li.get("quantity")) for li in line_items]
        return False, (
            f"No line item with qty 5 and unitPrice ~$49.95 (Widget B) found. Items: {items}."
        )

    return True, (
        f"QU-0028 declined. New quote '{new_quo.get('number')}' for Metro Fabrication Works "
        f"with 5 Widget B units, sent."
    )
