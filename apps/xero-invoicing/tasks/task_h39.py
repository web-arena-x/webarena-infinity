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

    # Atlas Engineering Consultants = con_025
    new_inv = None
    for inv in state.get("invoices", []):
        if inv.get("contactId") == "con_025" and inv.get("id") not in SEED_INVOICE_IDS:
            new_inv = inv
            break

    if new_inv is None:
        return False, "No new invoice found for Atlas Engineering Consultants (con_025)."

    line_items = new_inv.get("lineItems", [])
    if len(line_items) < 2:
        return False, f"New invoice has {len(line_items)} line item(s), expected at least 2."

    found_design = False
    design_tracking_ok = False
    found_cables = False

    for li in line_items:
        price = float(li.get("unitPrice", 0))
        qty = li.get("quantity", 0)

        if abs(price - 165.00) < 5.00 and qty == 3:
            found_design = True
            region = li.get("trackingRegion", "")
            dept = li.get("trackingDept", "")
            if region == "Victoria" and dept == "Sales":
                design_tracking_ok = True

        if abs(price - 12.50) < 2.00 and qty == 10:
            found_cables = True

    if not found_design:
        items = [(li.get("unitPrice"), li.get("quantity")) for li in line_items]
        return False, (
            f"No line item with qty 3 and unitPrice ~$165 (UI/UX design) found. Items: {items}."
        )

    if not design_tracking_ok:
        design_li = None
        for li in line_items:
            if abs(float(li.get("unitPrice", 0)) - 165.00) < 5.00:
                design_li = li
                break
        region = design_li.get("trackingRegion", "") if design_li else "?"
        dept = design_li.get("trackingDept", "") if design_li else "?"
        return False, (
            f"Design line item tracking is region='{region}', dept='{dept}', "
            f"expected region='Victoria', dept='Sales'."
        )

    if not found_cables:
        items = [(li.get("unitPrice"), li.get("quantity")) for li in line_items]
        return False, (
            f"No line item with qty 10 and unitPrice ~$12.50 (USB-C cables) found. Items: {items}."
        )

    return True, (
        f"Invoice '{new_inv.get('number')}' created for Atlas Engineering: "
        f"3 hrs UI/UX design ($165/hr, Victoria/Sales tracking) + 10 USB-C cables ($12.50)."
    )
