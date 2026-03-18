"""Verify: Approve all awaiting-approval invoices with reference starting with PO-."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    state = requests.get(f"{server_url}/api/state", timeout=5).json()
    invoices = state.get("invoices", [])

    # In seed state, inv_77 is the only awaiting_approval with PO- reference
    target_ids = ["inv_77"]
    errors = []

    for inv_id in target_ids:
        inv = next((i for i in invoices if i["id"] == inv_id), None)
        if not inv:
            errors.append(f"Invoice {inv_id} not found")
            continue
        if inv["status"] != "awaiting_payment":
            errors.append(f"Invoice {inv['invoiceNumber']} ({inv_id}) has status '{inv['status']}', expected 'awaiting_payment'")

    # Verify no awaiting_approval invoices with PO- reference remain
    remaining = [i for i in invoices if i["status"] == "awaiting_approval"
                 and i.get("reference", "").startswith("PO-")]
    if remaining:
        nums = [i["invoiceNumber"] for i in remaining]
        errors.append(f"Still awaiting approval with PO- ref: {', '.join(nums)}")

    if errors:
        return False, "; ".join(errors)
    return True, f"All {len(target_ids)} awaiting-approval invoice(s) with PO- reference approved"
