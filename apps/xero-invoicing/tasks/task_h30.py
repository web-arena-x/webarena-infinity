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

    # Harbour City Plumbing = con_021
    new_inv = None
    for inv in state.get("invoices", []):
        if inv.get("contactId") == "con_021" and inv.get("id") not in SEED_INVOICE_IDS:
            new_inv = inv
            break

    if new_inv is None:
        return False, "No new invoice found for Harbour City Plumbing (con_021)."

    status = new_inv.get("status", "")
    if status != "awaiting_payment":
        return False, (
            f"New invoice status is '{status}', expected 'awaiting_payment' (approved)."
        )

    theme_id = new_inv.get("brandingThemeId", "")
    if theme_id != "theme_professional":
        return False, (
            f"New invoice brandingThemeId is '{theme_id}', "
            f"expected 'theme_professional' (Professional Services)."
        )

    line_items = new_inv.get("lineItems", [])
    if len(line_items) < 2:
        return False, f"New invoice has {len(line_items)} line item(s), expected at least 2."

    found_audit = False
    found_dev = False
    for li in line_items:
        price = float(li.get("unitPrice", 0))
        qty = li.get("quantity", 0)
        if abs(price - 5500.00) < 10.00:
            found_audit = True
        if abs(price - 185.00) < 5.00 and qty == 16:
            found_dev = True

    if not found_audit:
        prices = [li.get("unitPrice") for li in line_items]
        return False, f"No line item with unitPrice ~$5,500 (security audit) found. Prices: {prices}."

    if not found_dev:
        items = [(li.get("unitPrice"), li.get("quantity")) for li in line_items]
        return False, f"No line item with qty 16 and unitPrice ~$185 (development) found. Items: {items}."

    return True, (
        f"Invoice '{new_inv.get('number')}' created for Harbour City Plumbing: "
        f"security audit ($5,500) + 16 hrs development ($185/hr), "
        f"Professional Services template, approved."
    )
