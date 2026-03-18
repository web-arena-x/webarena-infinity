import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Create a new invoice for Ironclad Security Systems with 2 line items, dated 2026-03-18, due 2026-04-17, reference SEC-2026-001, branding Bold Corporate. Approve and send."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    invoices = state.get("invoices", [])

    # Known original invoice IDs for con_16 (Ironclad Security Systems) to exclude
    original_inv_ids = {"inv_16", "inv_41", "inv_66", "inv_91"}

    # Find a NEW invoice for con_16 that is not one of the originals
    new_inv = None
    for inv in invoices:
        if inv.get("contactId") == "con_16" and inv.get("id") not in original_inv_ids:
            new_inv = inv
            break

    if new_inv is None:
        return False, "No new invoice found for Ironclad Security Systems (con_16)"

    errors = []
    inv_num = new_inv.get("invoiceNumber", new_inv.get("id"))

    # Check status
    status = new_inv.get("status")
    if status != "awaiting_payment":
        errors.append(f"Invoice {inv_num} has status '{status}', expected 'awaiting_payment'")

    # Check sentAt
    sent_at = new_inv.get("sentAt")
    if sent_at is None:
        errors.append(f"Invoice {inv_num} has sentAt=None, expected a timestamp (should be sent)")

    # Check reference
    ref = new_inv.get("reference")
    if ref != "SEC-2026-001":
        errors.append(f"Invoice {inv_num} has reference '{ref}', expected 'SEC-2026-001'")

    # Check branding theme
    branding = new_inv.get("brandingThemeId")
    if branding != "theme_4":
        errors.append(f"Invoice {inv_num} has brandingThemeId '{branding}', expected 'theme_4' (Bold Corporate)")

    # Check dates
    issue_date = new_inv.get("issueDate")
    if issue_date != "2026-03-18":
        errors.append(f"Invoice {inv_num} has issueDate '{issue_date}', expected '2026-03-18'")

    due_date = new_inv.get("dueDate")
    if due_date != "2026-04-17":
        errors.append(f"Invoice {inv_num} has dueDate '{due_date}', expected '2026-04-17'")

    # Check line items
    line_items = new_inv.get("lineItems", [])
    if len(line_items) != 2:
        errors.append(f"Invoice {inv_num} has {len(line_items)} line items, expected 2")
    else:
        # Sort line items by description for consistent checking
        items_lower = [(li.get("description", "").lower().strip(), li) for li in line_items]

        found_cctv = False
        found_monitoring = False

        for desc_lower, li in items_lower:
            if "cctv" in desc_lower and "install" in desc_lower:
                found_cctv = True
                qty = li.get("quantity", 0)
                price = li.get("unitPrice", li.get("unitAmount", 0))
                if abs(qty - 8) > 0.01:
                    errors.append(f"CCTV installation line item has quantity {qty}, expected 8")
                if abs(price - 450) > 0.01:
                    errors.append(f"CCTV installation line item has unitPrice {price}, expected 450")
            elif "monitor" in desc_lower and "subscri" in desc_lower:
                found_monitoring = True
                qty = li.get("quantity", 0)
                price = li.get("unitPrice", li.get("unitAmount", 0))
                if abs(qty - 1) > 0.01:
                    errors.append(f"Monitoring subscription line item has quantity {qty}, expected 1")
                if abs(price - 2400) > 0.01:
                    errors.append(f"Monitoring subscription line item has unitPrice {price}, expected 2400")

        if not found_cctv:
            errors.append("Missing line item for 'CCTV installation'")
        if not found_monitoring:
            errors.append("Missing line item for 'monitoring subscription'")

    if errors:
        return False, "; ".join(errors)

    return True, f"New invoice {inv_num} for Ironclad Security Systems created, approved, and sent with correct details"
