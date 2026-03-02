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

    settings = state.get("invoiceSettings", {})

    # Check prefix changed to DEMO-
    prefix = settings.get("invoicePrefix", "")
    if prefix != "DEMO-":
        return False, f"Invoice prefix is '{prefix}', expected 'DEMO-'."

    # Check next number set to 200
    next_num = settings.get("invoiceNextNumber")
    # After creating one invoice, next number should be 201
    if next_num is not None and next_num < 200:
        return False, (
            f"Invoice next number is {next_num}, expected >= 200."
        )

    # Find new invoice for Greenfield Organics (con_003) with DEMO- prefix
    new_inv = None
    for inv in state.get("invoices", []):
        if inv.get("contactId") == "con_003" and inv.get("id") not in SEED_INVOICE_IDS:
            new_inv = inv
            break

    if new_inv is None:
        return False, (
            "No new invoice found for Greenfield Organics (con_003)."
        )

    inv_number = new_inv.get("number", "")
    if not inv_number.startswith("DEMO-"):
        return False, (
            f"New invoice number is '{inv_number}', expected to start with 'DEMO-'."
        )

    # Check line item: on-site training at ~$2,200
    line_items = new_inv.get("lineItems", [])
    found = False
    for li in line_items:
        price = float(li.get("unitPrice", 0))
        if abs(price - 2200.00) < 50.00:
            found = True
            break

    if not found:
        items = [(li.get("unitPrice"), li.get("quantity")) for li in line_items]
        return False, (
            f"No line item with unitPrice ~$2,200 (on-site training) found. Items: {items}."
        )

    return True, (
        f"Invoice prefix changed to 'DEMO-', numbering from 200. "
        f"New invoice '{inv_number}' created for Greenfield Organics with on-site training."
    )
