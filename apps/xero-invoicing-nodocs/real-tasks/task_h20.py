import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Create contact Pacific Digital Solutions and create a draft invoice with 3 line items."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    contacts = state.get("contacts", [])
    invoices = state.get("invoices", [])

    # Find contact 'Pacific Digital Solutions'
    target_contact = None
    for c in contacts:
        if c.get("name", "").strip().lower() == "pacific digital solutions":
            target_contact = c
            break

    if target_contact is None:
        return False, "Contact 'Pacific Digital Solutions' not found"

    errors = []
    con_id = target_contact.get("id")

    # Check contact details
    email = target_contact.get("email", "")
    if email != "billing@pacificdigital.co.nz":
        errors.append(f"Contact email is '{email}', expected 'billing@pacificdigital.co.nz'")

    phone = target_contact.get("phone", "")
    # Normalize phone for comparison (strip spaces)
    phone_normalized = phone.replace(" ", "").replace("-", "")
    expected_phone_normalized = "+6498887777"
    if phone_normalized != expected_phone_normalized:
        errors.append(f"Contact phone is '{phone}', expected '+64 9 888 7777'")

    # Check address
    address = target_contact.get("billingAddress", target_contact.get("address", {}))
    addr_line = address.get("addressLine1", address.get("street", ""))
    if "55" not in str(addr_line) or "victoria" not in str(addr_line).lower():
        errors.append(f"Contact address line is '{addr_line}', expected '55 Victoria Street West'")

    city = address.get("city", "")
    if city.lower() != "auckland":
        errors.append(f"Contact city is '{city}', expected 'Auckland'")

    postal_code = address.get("postalCode", "")
    if str(postal_code) != "1010":
        errors.append(f"Contact postalCode is '{postal_code}', expected '1010'")

    country = address.get("country", "")
    if "new zealand" not in country.lower() and "nz" not in country.lower():
        errors.append(f"Contact country is '{country}', expected 'New Zealand'")

    # Find a draft invoice for this contact
    draft_inv = None
    for inv in invoices:
        if inv.get("contactId") == con_id and inv.get("status") == "draft":
            draft_inv = inv
            break

    if draft_inv is None:
        return False, f"No draft invoice found for Pacific Digital Solutions ({con_id})" + (
            "; " + "; ".join(errors) if errors else ""
        )

    inv_num = draft_inv.get("invoiceNumber", draft_inv.get("id"))

    # Check dates
    issue_date = draft_inv.get("issueDate")
    if issue_date != "2026-03-18":
        errors.append(f"Invoice {inv_num} has issueDate '{issue_date}', expected '2026-03-18'")

    due_date = draft_inv.get("dueDate")
    if due_date != "2026-04-17":
        errors.append(f"Invoice {inv_num} has dueDate '{due_date}', expected '2026-04-17'")

    # Check 3 line items
    line_items = draft_inv.get("lineItems", [])
    if len(line_items) != 3:
        errors.append(f"Invoice {inv_num} has {len(line_items)} line items, expected 3")
    else:
        found_website = False
        found_seo = False
        found_content = False

        for li in line_items:
            desc = (li.get("description") or "").lower().strip()
            qty = li.get("quantity", 0)
            price = li.get("unitPrice", li.get("unitAmount", 0))

            if "website" in desc and "redesign" in desc:
                found_website = True
                if abs(qty - 1) > 0.01:
                    errors.append(f"Website redesign line item has quantity {qty}, expected 1")
                if abs(price - 8000) > 0.01:
                    errors.append(f"Website redesign line item has unitPrice {price}, expected 8000")
            elif "seo" in desc and "package" in desc:
                found_seo = True
                if abs(qty - 6) > 0.01:
                    errors.append(f"SEO package line item has quantity {qty}, expected 6")
                if abs(price - 500) > 0.01:
                    errors.append(f"SEO package line item has unitPrice {price}, expected 500")
            elif "content" in desc and "writ" in desc:
                found_content = True
                if abs(qty - 10) > 0.01:
                    errors.append(f"Content writing line item has quantity {qty}, expected 10")
                if abs(price - 150) > 0.01:
                    errors.append(f"Content writing line item has unitPrice {price}, expected 150")

        if not found_website:
            errors.append("Missing line item for 'Website redesign'")
        if not found_seo:
            errors.append("Missing line item for 'SEO package'")
        if not found_content:
            errors.append("Missing line item for 'Content writing'")

    if errors:
        return False, "; ".join(errors)

    return True, f"Contact Pacific Digital Solutions created and draft invoice {inv_num} with 3 line items verified"
