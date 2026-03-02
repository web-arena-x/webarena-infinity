import requests


SEED_INVOICE_IDS = {
    "inv_000", "inv_001", "inv_002", "inv_003", "inv_004", "inv_005",
    "inv_006", "inv_007", "inv_008", "inv_009", "inv_010", "inv_011",
    "inv_012", "inv_013", "inv_014", "inv_015", "inv_016", "inv_017",
    "inv_018", "inv_019", "inv_020", "inv_021", "inv_022", "inv_023",
    "inv_024", "inv_025",
}


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # The client with the highest overdue invoice total is CloudNine Analytics (con_007),
    # whose INV-0047 ($18,652.70) is by far the largest overdue invoice.
    # A new invoice should be created for them with a software license item (~$1,200).
    new_inv = None
    for inv in state.get("invoices", []):
        if inv.get("contactId") == "con_007" and inv.get("id") not in SEED_INVOICE_IDS:
            new_inv = inv
            break

    if new_inv is None:
        return False, (
            "No new invoice found for CloudNine Analytics (con_007). "
            "They have the highest overdue invoice total (INV-0047 at $18,652.70)."
        )

    # Check line item: software license at ~$1,200
    line_items = new_inv.get("lineItems", [])
    found = False
    for li in line_items:
        price = float(li.get("unitPrice", 0))
        qty = li.get("quantity", 0)
        if abs(price - 1200.00) < 50.00 and qty >= 1:
            found = True
            break

    if not found:
        items = [(li.get("unitPrice"), li.get("quantity")) for li in line_items]
        return False, (
            f"No line item with unitPrice ~$1,200 (software license) found. Items: {items}."
        )

    return True, (
        f"New invoice '{new_inv.get('number')}' created for CloudNine Analytics "
        f"(highest overdue invoice total) for annual software license renewal."
    )
