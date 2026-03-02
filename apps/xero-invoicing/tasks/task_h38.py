import requests


# Seed invoice IDs
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

    # Northern Territory Power Corp = con_017
    new_inv = None
    for inv in state.get("invoices", []):
        if inv.get("contactId") == "con_017" and inv.get("id") not in SEED_INVOICE_IDS:
            new_inv = inv
            break

    if new_inv is None:
        return False, "No new invoice found for Northern Territory Power Corp (con_017)."

    status = new_inv.get("status", "")
    if status != "awaiting_payment":
        return False, (
            f"New invoice status is '{status}', expected 'awaiting_payment' (approved)."
        )

    sent_at = new_inv.get("sentAt")
    if sent_at is None:
        return False, "New invoice has not been sent (sentAt is None)."

    line_items = new_inv.get("lineItems", [])
    if len(line_items) < 2:
        return False, f"New invoice has {len(line_items)} line item(s), expected at least 2."

    found_migration = False
    found_setup = False
    for li in line_items:
        price = float(li.get("unitPrice", 0))
        if abs(price - 3800.00) < 10.00:
            found_migration = True
        if abs(price - 500.00) < 10.00:
            found_setup = True

    if not found_migration:
        prices = [li.get("unitPrice") for li in line_items]
        return False, f"No line item with unitPrice ~$3,800 (data migration) found. Prices: {prices}."

    if not found_setup:
        prices = [li.get("unitPrice") for li in line_items]
        return False, f"No line item with unitPrice ~$500 (setup fee) found. Prices: {prices}."

    return True, (
        f"Invoice '{new_inv.get('number')}' created for Northern Territory Power Corp: "
        f"data migration ($3,800) + setup fee ($500), approved and sent."
    )
