"""Verify: PROJ-ALPHA awaiting-approval invoice (inv_112) — add line item, approve, send."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    state = requests.get(f"{server_url}/api/state", timeout=5).json()
    invoices = state.get("invoices", [])

    inv = next((i for i in invoices if i["id"] == "inv_112"), None)
    if not inv:
        return False, "Invoice inv_112 not found"

    errors = []

    # Should be approved (awaiting_payment)
    if inv["status"] != "awaiting_payment":
        errors.append(f"Status is '{inv['status']}', expected 'awaiting_payment'")

    # Should be sent
    if not inv.get("sentAt"):
        errors.append("sentAt is null — invoice not sent")

    # Should have 5 line items (4 original + 1 new)
    lis = inv.get("lineItems", [])
    if len(lis) < 5:
        errors.append(f"Expected at least 5 line items, found {len(lis)}")

    # Check for the new line item
    closeout = next((l for l in lis if "closeout" in l.get("description", "").lower()
                      or "project" in l.get("description", "").lower()
                      and "documentation" in l.get("description", "").lower()), None)
    if not closeout:
        # Also check by quantity/price
        closeout = next((l for l in lis if abs(l.get("quantity", 0) - 5) < 0.01
                          and abs(l.get("unitPrice", 0) - 120) < 0.01), None)
    if not closeout:
        errors.append("No line item matching 'Project closeout documentation' (5 x $120) found")
    else:
        if abs(closeout.get("quantity", 0) - 5) > 0.01:
            errors.append(f"New line item quantity is {closeout.get('quantity')}, expected 5")
        if abs(closeout.get("unitPrice", 0) - 120) > 0.01:
            errors.append(f"New line item unitPrice is {closeout.get('unitPrice')}, expected 120")

    if errors:
        return False, "; ".join(errors)
    return True, "PROJ-ALPHA invoice updated with new line item, approved, and sent"
