"""Verify: Create Alpine Adventure Tours contact and approved invoice with 2 line items."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    state = requests.get(f"{server_url}/api/state", timeout=5).json()
    contacts = state.get("contacts", [])
    invoices = state.get("invoices", [])

    errors = []

    # Check contact
    con = next((c for c in contacts if c["name"] == "Alpine Adventure Tours"), None)
    if not con:
        return False, "Contact 'Alpine Adventure Tours' not found"

    if con.get("email") != "bookings@alpineadventure.co.nz":
        errors.append(f"Contact email is '{con.get('email')}', expected 'bookings@alpineadventure.co.nz'")
    phone = (con.get("phone") or "").replace(" ", "")
    if phone != "+6434425678":
        errors.append(f"Contact phone is '{con.get('phone')}', expected '+64 3 442 5678'")
    addr = con.get("billingAddress", {})
    if addr.get("city") != "Queenstown":
        errors.append(f"Billing city is '{addr.get('city')}', expected 'Queenstown'")
    if addr.get("postalCode") != "9300":
        errors.append(f"Postal code is '{addr.get('postalCode')}', expected '9300'")
    if con.get("taxId") != "NZ-55-123-456":
        errors.append(f"Tax ID is '{con.get('taxId')}', expected 'NZ-55-123-456'")

    # Check invoice
    con_invoices = [i for i in invoices if i["contactId"] == con["id"]]
    approved = [i for i in con_invoices if i["status"] == "awaiting_payment"]
    if not approved:
        errors.append("No approved invoice found for Alpine Adventure Tours")
    else:
        inv = approved[0]
        if inv.get("reference") != "TOUR-2026-01":
            errors.append(f"Invoice reference is '{inv.get('reference')}', expected 'TOUR-2026-01'")
        if inv.get("issueDate") != "2026-03-18":
            errors.append(f"Issue date is '{inv.get('issueDate')}', expected '2026-03-18'")
        if inv.get("dueDate") != "2026-04-17":
            errors.append(f"Due date is '{inv.get('dueDate')}', expected '2026-04-17'")

        lis = inv.get("lineItems", [])
        if len(lis) < 2:
            errors.append(f"Expected 2 line items, found {len(lis)}")
        else:
            # Check guided tour line item
            tour = next((l for l in lis if "tour" in l.get("description", "").lower()), None)
            if not tour:
                errors.append("No line item matching 'tour' found")
            elif abs(tour["quantity"] - 10) > 0.01 or abs(tour["unitPrice"] - 350) > 0.01:
                errors.append(f"Tour line item: qty={tour['quantity']} price={tour['unitPrice']}, expected 10 x $350")

            # Check equipment hire line item
            equip = next((l for l in lis if "equipment" in l.get("description", "").lower()), None)
            if not equip:
                errors.append("No line item matching 'equipment' found")
            elif abs(equip["quantity"] - 3) > 0.01 or abs(equip["unitPrice"] - 200) > 0.01:
                errors.append(f"Equipment line item: qty={equip['quantity']} price={equip['unitPrice']}, expected 3 x $200")

    if errors:
        return False, "; ".join(errors)
    return True, "Alpine Adventure Tours contact and approved invoice created successfully"
