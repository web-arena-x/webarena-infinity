"""Verify: Void all overdue invoices denominated in AUD."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    state = requests.get(f"{server_url}/api/state", timeout=5).json()
    invoices = state.get("invoices", [])

    # In seed state: inv_33 (AUD overdue) and inv_102 (AUD overdue)
    target_ids = ["inv_33", "inv_102"]
    errors = []

    for inv_id in target_ids:
        inv = next((i for i in invoices if i["id"] == inv_id), None)
        if not inv:
            errors.append(f"Invoice {inv_id} not found")
            continue
        if inv["status"] != "voided":
            errors.append(f"Invoice {inv['invoiceNumber']} ({inv_id}) has status '{inv['status']}', expected 'voided'")
        if not inv.get("voidedAt"):
            errors.append(f"Invoice {inv['invoiceNumber']} ({inv_id}) is missing voidedAt timestamp")

    # Verify no AUD overdue remain
    remaining = [i for i in invoices if i["status"] == "overdue" and i.get("currency") == "AUD"]
    if remaining:
        nums = [i["invoiceNumber"] for i in remaining]
        errors.append(f"Still overdue AUD invoices: {', '.join(nums)}")

    if errors:
        return False, "; ".join(errors)
    return True, f"All {len(target_ids)} overdue AUD invoice(s) voided"
