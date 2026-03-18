import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Add a line item to draft invoice INV-0083 for Metro Print Solutions: 'Express delivery surcharge', qty 1, unit price $150."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    invoices = state.get("invoices", [])
    target = None
    for inv in invoices:
        if inv.get("id") == "inv_83" or inv.get("invoiceNumber") == "INV-0083":
            target = inv
            break

    if target is None:
        return False, "Invoice INV-0083 not found in state"

    line_items = target.get("lineItems", [])
    if not line_items:
        return False, "Invoice INV-0083 has no line items"

    # Look for the new line item (case-insensitive match)
    found = None
    for item in line_items:
        desc = (item.get("description") or "").strip().lower()
        if "express delivery surcharge" in desc:
            found = item
            break

    if found is None:
        descriptions = [item.get("description", "") for item in line_items]
        return False, f"No line item with description containing 'Express delivery surcharge' found. Existing descriptions: {descriptions}"

    errors = []

    qty = found.get("quantity")
    if qty is not None:
        try:
            if abs(float(qty) - 1) > 0.01:
                errors.append(f"Quantity is {qty}, expected 1")
        except (ValueError, TypeError):
            errors.append(f"Quantity '{qty}' is not a valid number")

    unit_price = found.get("unitPrice")
    if unit_price is not None:
        try:
            if abs(float(unit_price) - 150) > 0.01:
                errors.append(f"Unit price is {unit_price}, expected 150")
        except (ValueError, TypeError):
            errors.append(f"Unit price '{unit_price}' is not a valid number")

    if errors:
        return False, "; ".join(errors)

    return True, "Line item 'Express delivery surcharge' (qty 1, $150) found on invoice INV-0083"
