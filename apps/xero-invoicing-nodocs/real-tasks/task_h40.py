"""Verify: Create Summit Events contact, create invoice, approve and send."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    state = requests.get(f"{server_url}/api/state", timeout=5).json()
    contacts = state.get("contacts", [])
    invoices = state.get("invoices", [])

    errors = []

    # Check contact
    con = next((c for c in contacts if c["name"] == "Summit Events Ltd"), None)
    if not con:
        return False, "Contact 'Summit Events Ltd' not found"

    if con.get("email") != "events@summitevents.co.nz":
        errors.append(f"Contact email is '{con.get('email')}', expected 'events@summitevents.co.nz'")
    phone = (con.get("phone") or "").replace(" ", "")
    if phone != "+6495553456":
        errors.append(f"Contact phone is '{con.get('phone')}', expected '+64 9 555 3456'")
    addr = con.get("billingAddress", {})
    if addr.get("city") != "Auckland":
        errors.append(f"Billing city is '{addr.get('city')}', expected 'Auckland'")

    # Check invoice
    con_invoices = [i for i in invoices if i.get("contactId") == con["id"]]
    if not con_invoices:
        errors.append("No invoice found for Summit Events Ltd")
    else:
        inv = con_invoices[0]
        if inv.get("status") != "awaiting_payment":
            errors.append(f"Invoice status is '{inv.get('status')}', expected 'awaiting_payment'")
        if not inv.get("sentAt"):
            errors.append("Invoice sentAt is null — not sent")
        if inv.get("reference") != "EVT-2026-001":
            errors.append(f"Reference is '{inv.get('reference')}', expected 'EVT-2026-001'")
        if inv.get("issueDate") != "2026-03-18":
            errors.append(f"Issue date is '{inv.get('issueDate')}', expected '2026-03-18'")
        if inv.get("dueDate") != "2026-04-17":
            errors.append(f"Due date is '{inv.get('dueDate')}', expected '2026-04-17'")

        lis = inv.get("lineItems", [])
        if len(lis) < 3:
            errors.append(f"Expected 3 line items, found {len(lis)}")
        else:
            # Venue hire
            venue = next((l for l in lis if "venue" in l.get("description", "").lower()), None)
            if not venue:
                errors.append("No 'venue' line item found")
            elif abs(venue["quantity"] - 1) > 0.01 or abs(venue["unitPrice"] - 2500) > 0.01:
                errors.append(f"Venue line: qty={venue['quantity']} price={venue['unitPrice']}, expected 1 x $2,500")

            # Catering
            catering = next((l for l in lis if "catering" in l.get("description", "").lower()), None)
            if not catering:
                errors.append("No 'catering' line item found")
            elif abs(catering["quantity"] - 50) > 0.01 or abs(catering["unitPrice"] - 85) > 0.01:
                errors.append(f"Catering line: qty={catering['quantity']} price={catering['unitPrice']}, expected 50 x $85")

            # AV equipment
            av = next((l for l in lis if "av" in l.get("description", "").lower()
                        or "audio" in l.get("description", "").lower()
                        or "equipment" in l.get("description", "").lower()), None)
            if not av:
                errors.append("No 'AV equipment' line item found")
            elif abs(av["quantity"] - 1) > 0.01 or abs(av["unitPrice"] - 1200) > 0.01:
                errors.append(f"AV line: qty={av['quantity']} price={av['unitPrice']}, expected 1 x $1,200")

    if errors:
        return False, "; ".join(errors)
    return True, "Summit Events Ltd contact and approved+sent invoice created successfully"
