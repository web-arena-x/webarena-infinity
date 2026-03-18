import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Create a new invoice for Nexus Technologies Ltd with three line items."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    invoices = state.get("invoices", [])

    # Known original invoice IDs for con_4
    original_ids = {"inv_4", "inv_29", "inv_54", "inv_79", "inv_104"}

    # Find new invoices for Nexus Technologies Ltd (con_4)
    new_invoices = []
    for inv in invoices:
        if inv.get("contactId") == "con_4" and inv.get("id") not in original_ids:
            new_invoices.append(inv)

    if not new_invoices:
        return False, "No new invoice found for Nexus Technologies Ltd (con_4)"

    errors = []
    found_match = False

    for inv in new_invoices:
        inv_errors = []

        status = inv.get("status")
        if status != "awaiting_payment":
            inv_errors.append(f"status is '{status}', expected 'awaiting_payment'")

        issue_date = inv.get("issueDate")
        if issue_date != "2026-03-18":
            inv_errors.append(f"issueDate is '{issue_date}', expected '2026-03-18'")

        due_date = inv.get("dueDate")
        if due_date != "2026-04-07":
            inv_errors.append(f"dueDate is '{due_date}', expected '2026-04-07'")

        reference = inv.get("reference", "")
        if reference != "PROJ-NEXUS-01":
            inv_errors.append(f"reference is '{reference}', expected 'PROJ-NEXUS-01'")

        line_items = inv.get("lineItems", [])
        if len(line_items) != 3:
            inv_errors.append(f"has {len(line_items)} line items, expected 3")
        else:
            expected_items = [
                {"desc": "Cloud migration", "qty": 40, "price": 200},
                {"desc": "Database optimization", "qty": 16, "price": 250},
                {"desc": "Security audit", "qty": 8, "price": 300},
            ]

            for expected in expected_items:
                matched = False
                for li in line_items:
                    desc = li.get("description", "")
                    if expected["desc"].lower() in desc.lower():
                        qty = li.get("quantity")
                        price = li.get("unitPrice") or li.get("unitAmount")
                        if qty != expected["qty"]:
                            inv_errors.append(
                                f"Line '{expected['desc']}' quantity is {qty}, expected {expected['qty']}"
                            )
                        if price != expected["price"]:
                            inv_errors.append(
                                f"Line '{expected['desc']}' unit price is {price}, expected {expected['price']}"
                            )
                        matched = True
                        break
                if not matched:
                    inv_errors.append(f"No line item containing '{expected['desc']}' found")

        if not inv_errors:
            found_match = True
            break
        else:
            errors.extend(inv_errors)

    if found_match:
        return True, "New invoice for Nexus Technologies Ltd created correctly with all 3 line items"

    return False, "New invoice issues: " + "; ".join(errors)
