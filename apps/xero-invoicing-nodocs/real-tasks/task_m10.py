import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Create a new draft invoice for Ridgeway University with one line item: 'Annual subscription renewal' qty 1 at $4,500, dated 2026-03-18, due 2026-04-17."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    invoices = state.get("invoices", [])

    # Known original invoice IDs for Ridgeway University (con_1) — exclude these
    # We look for any new invoice for con_1 that is a draft
    candidates = []
    for inv in invoices:
        if inv.get("contactId") == "con_1" and inv.get("status") == "draft":
            candidates.append(inv)

    if not candidates:
        return False, "No draft invoice found for Ridgeway University (con_1)"

    # Look for a candidate that matches our criteria
    for inv in candidates:
        errors = []

        issue_date = inv.get("issueDate", "")
        if issue_date != "2026-03-18":
            errors.append(f"issueDate is '{issue_date}', expected '2026-03-18'")

        due_date = inv.get("dueDate", "")
        if due_date != "2026-04-17":
            errors.append(f"dueDate is '{due_date}', expected '2026-04-17'")

        line_items = inv.get("lineItems", [])
        found_item = None
        for item in line_items:
            desc = (item.get("description") or "").strip().lower()
            if "annual subscription renewal" in desc:
                found_item = item
                break

        if found_item is None:
            errors.append("No line item with description containing 'Annual subscription renewal'")
        else:
            qty = found_item.get("quantity")
            if qty is not None:
                try:
                    if abs(float(qty) - 1) > 0.01:
                        errors.append(f"Line item quantity is {qty}, expected 1")
                except (ValueError, TypeError):
                    errors.append(f"Line item quantity '{qty}' is not a valid number")

            unit_price = found_item.get("unitPrice")
            if unit_price is not None:
                try:
                    if abs(float(unit_price) - 4500) > 0.01:
                        errors.append(f"Line item unitPrice is {unit_price}, expected 4500")
                except (ValueError, TypeError):
                    errors.append(f"Line item unitPrice '{unit_price}' is not a valid number")

        if not errors:
            return True, f"New draft invoice (id={inv.get('id')}) for Ridgeway University with correct dates and line item found"

    # If we get here, none of the candidates matched perfectly. Report errors from the last one.
    # Try again and collect all candidates' issues for a better error message
    all_issues = []
    for inv in candidates:
        inv_errors = []
        if inv.get("issueDate") != "2026-03-18":
            inv_errors.append(f"issueDate={inv.get('issueDate')}")
        if inv.get("dueDate") != "2026-04-17":
            inv_errors.append(f"dueDate={inv.get('dueDate')}")
        line_items = inv.get("lineItems", [])
        has_item = any("annual subscription renewal" in (li.get("description") or "").lower() for li in line_items)
        if not has_item:
            inv_errors.append("missing 'Annual subscription renewal' line item")
        all_issues.append(f"Invoice {inv.get('id')}: {', '.join(inv_errors) if inv_errors else 'unknown issue'}")

    return False, "Draft invoice(s) found for con_1 but none match all criteria: " + "; ".join(all_issues)
