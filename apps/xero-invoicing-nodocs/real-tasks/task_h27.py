"""Verify: Full payments for all overdue invoices of contact on Ponsonby Road (Bloom & Branch)."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    state = requests.get(f"{server_url}/api/state", timeout=5).json()
    invoices = state.get("invoices", [])
    payments = state.get("payments", [])

    # Bloom & Branch Florists (con_15) at 103 Ponsonby Road
    # Overdue invoices: inv_15 and inv_40
    target_ids = ["inv_15", "inv_40"]
    errors = []

    for inv_id in target_ids:
        inv = next((i for i in invoices if i["id"] == inv_id), None)
        if not inv:
            errors.append(f"Invoice {inv_id} not found")
            continue
        if inv["status"] != "paid":
            errors.append(f"Invoice {inv['invoiceNumber']} ({inv_id}) status is '{inv['status']}', expected 'paid'")
        if abs(inv.get("amountDue", 999)) > 0.01:
            errors.append(f"Invoice {inv['invoiceNumber']} ({inv_id}) amountDue is {inv.get('amountDue')}, expected 0")

        inv_pays = [p for p in payments if p["invoiceId"] == inv_id]
        bank1_pays = [p for p in inv_pays if p.get("bankAccountId") == "bank_1"]
        if not bank1_pays:
            errors.append(f"No payment via Business Cheque Account for {inv_id}")

    if errors:
        return False, "; ".join(errors)
    return True, f"Full payments recorded for {len(target_ids)} overdue invoice(s) of Ponsonby Road contact"
