"""Verify: Create AUD invoice for Australia contact (CloudBridge) and approve it."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    state = requests.get(f"{server_url}/api/state", timeout=5).json()
    invoices = state.get("invoices", [])

    # CloudBridge Software is con_21 (Australia)
    seed_ids = {f"inv_{n}" for n in range(1, 114)}
    new_invoices = [i for i in invoices
                    if i["id"] not in seed_ids
                    and i["contactId"] == "con_21"]

    if not new_invoices:
        return False, "No new invoice found for CloudBridge Software (con_21)"

    errors = []
    inv = new_invoices[0]

    if inv.get("status") != "awaiting_payment":
        errors.append(f"Status is '{inv.get('status')}', expected 'awaiting_payment'")
    if inv.get("currency") != "AUD":
        errors.append(f"Currency is '{inv.get('currency')}', expected 'AUD'")
    if inv.get("reference") != "AU-REVIEW-001":
        errors.append(f"Reference is '{inv.get('reference')}', expected 'AU-REVIEW-001'")
    if inv.get("issueDate") != "2026-03-18":
        errors.append(f"Issue date is '{inv.get('issueDate')}', expected '2026-03-18'")
    if inv.get("dueDate") != "2026-05-18":
        errors.append(f"Due date is '{inv.get('dueDate')}', expected '2026-05-18'")

    lis = inv.get("lineItems", [])
    if len(lis) < 2:
        errors.append(f"Expected 2 line items, found {len(lis)}")
    else:
        arch = next((l for l in lis if "architecture" in l.get("description", "").lower()
                      or "review" in l.get("description", "").lower()), None)
        if not arch:
            errors.append("No line item matching 'architecture review' found")
        elif abs(arch["quantity"] - 8) > 0.01 or abs(arch["unitPrice"] - 300) > 0.01:
            errors.append(f"Architecture line: qty={arch['quantity']} price={arch['unitPrice']}, expected 8 x $300")

        perf = next((l for l in lis if "performance" in l.get("description", "").lower()
                      or "testing" in l.get("description", "").lower()), None)
        if not perf:
            errors.append("No line item matching 'performance testing' found")
        elif abs(perf["quantity"] - 16) > 0.01 or abs(perf["unitPrice"] - 200) > 0.01:
            errors.append(f"Performance line: qty={perf['quantity']} price={perf['unitPrice']}, expected 16 x $200")

    if errors:
        return False, "; ".join(errors)
    return True, f"New AUD invoice (id={inv['id']}) created for CloudBridge and approved"
