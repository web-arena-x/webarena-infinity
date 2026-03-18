import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Create a new contact Tasman Engineering Ltd and create a draft invoice for them."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    contacts = state.get("contacts", [])
    invoices = state.get("invoices", [])

    # Find the new contact
    tasman_contact = None
    for c in contacts:
        if c.get("name") == "Tasman Engineering Ltd":
            tasman_contact = c
            break

    if tasman_contact is None:
        return False, "Contact 'Tasman Engineering Ltd' not found"

    errors = []

    # Verify contact details
    email = tasman_contact.get("email")
    if email != "accounts@tasmaneng.co.nz":
        errors.append(f"Contact email is '{email}', expected 'accounts@tasmaneng.co.nz'")

    phone = tasman_contact.get("phone")
    if phone != "+64 3 545 1234":
        errors.append(f"Contact phone is '{phone}', expected '+64 3 545 1234'")

    tax_id = tasman_contact.get("taxId") or tasman_contact.get("taxNumber")
    if tax_id != "NZ-45-678-901":
        errors.append(f"Contact taxId is '{tax_id}', expected 'NZ-45-678-901'")

    # Check billing address
    address = tasman_contact.get("billingAddress", {})
    if not isinstance(address, dict):
        errors.append(f"Contact billingAddress is not a dict: {address}")
    else:
        if address.get("street") != "25 Trafalgar Street":
            errors.append(f"Contact street is '{address.get('street')}', expected '25 Trafalgar Street'")
        if address.get("city") != "Nelson":
            errors.append(f"Contact city is '{address.get('city')}', expected 'Nelson'")
        if address.get("region") != "Nelson":
            errors.append(f"Contact region is '{address.get('region')}', expected 'Nelson'")
        if address.get("postalCode") != "7010":
            errors.append(f"Contact postalCode is '{address.get('postalCode')}', expected '7010'")
        if address.get("country") != "New Zealand":
            errors.append(f"Contact country is '{address.get('country')}', expected 'New Zealand'")

    # Find draft invoice for this contact
    contact_id = tasman_contact.get("id")
    draft_invoices = []
    for inv in invoices:
        if inv.get("contactId") == contact_id and inv.get("status") == "draft":
            draft_invoices.append(inv)

    if not draft_invoices:
        errors.append("No draft invoice found for Tasman Engineering Ltd")
        return False, "; ".join(errors)

    # Check the invoice details
    found_valid = False
    inv_errors = []

    for inv in draft_invoices:
        current_errors = []

        issue_date = inv.get("issueDate")
        if issue_date != "2026-03-18":
            current_errors.append(f"issueDate is '{issue_date}', expected '2026-03-18'")

        due_date = inv.get("dueDate")
        if due_date != "2026-04-17":
            current_errors.append(f"dueDate is '{due_date}', expected '2026-04-17'")

        line_items = inv.get("lineItems", [])
        if len(line_items) != 2:
            current_errors.append(f"has {len(line_items)} line items, expected 2")
        else:
            expected_items = [
                {"desc": "Structural engineering", "qty": 24, "price": 180},
                {"desc": "Site inspection", "qty": 1, "price": 750},
            ]

            for expected in expected_items:
                matched = False
                for li in line_items:
                    desc = li.get("description", "")
                    if expected["desc"].lower() in desc.lower():
                        qty = li.get("quantity")
                        price = li.get("unitPrice") or li.get("unitAmount")
                        if qty != expected["qty"]:
                            current_errors.append(
                                f"Line '{expected['desc']}' quantity is {qty}, expected {expected['qty']}"
                            )
                        if price != expected["price"]:
                            current_errors.append(
                                f"Line '{expected['desc']}' unit price is {price}, expected {expected['price']}"
                            )
                        matched = True
                        break
                if not matched:
                    current_errors.append(f"No line item containing '{expected['desc']}' found")

        if not current_errors:
            found_valid = True
            break
        else:
            inv_errors.extend(current_errors)

    if not found_valid:
        errors.extend(inv_errors)

    if errors:
        return False, "; ".join(errors)

    return True, "Contact 'Tasman Engineering Ltd' created and draft invoice with correct line items exists"
