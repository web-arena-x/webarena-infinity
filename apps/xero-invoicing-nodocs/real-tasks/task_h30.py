"""Verify: Approve awaiting-approval invoices for contacts that have overdue invoices."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    state = requests.get(f"{server_url}/api/state", timeout=5).json()
    invoices = state.get("invoices", [])

    # Contacts with overdue invoices: con_2, con_4, con_7, con_8, con_9, con_12, con_13, con_14, con_15, con_18, con_25
    # Of those, the ones that also have awaiting_approval:
    # con_2 → inv_77, con_7 → inv_32, con_8 → inv_8, con_12 → inv_112, con_13 → inv_38
    target_ids = ["inv_77", "inv_32", "inv_8", "inv_112", "inv_38"]
    errors = []

    for inv_id in target_ids:
        inv = next((i for i in invoices if i["id"] == inv_id), None)
        if not inv:
            errors.append(f"Invoice {inv_id} not found")
            continue
        if inv["status"] != "awaiting_payment":
            errors.append(f"Invoice {inv['invoiceNumber']} ({inv_id}) status is '{inv['status']}', expected 'awaiting_payment'")

    if errors:
        return False, "; ".join(errors)
    return True, f"All {len(target_ids)} awaiting-approval invoice(s) for contacts with overdue invoices approved"
