"""Verify: Full payments on all overdue invoices for Auckland-region contacts."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    state = requests.get(f"{server_url}/api/state", timeout=5).json()
    invoices = state.get("invoices", [])
    payments = state.get("payments", [])
    contacts = state.get("contacts", [])

    auckland_ids = {c["id"] for c in contacts if c.get("billingAddress", {}).get("region") == "Auckland"}

    # Overdue Auckland invoices in seed: inv_33 (con_8), inv_87 (con_12), inv_15 (con_15), inv_40 (con_15)
    target_ids = ["inv_33", "inv_87", "inv_15", "inv_40"]
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
        bank1 = [p for p in inv_pays if p.get("bankAccountId") == "bank_1"]
        if not bank1:
            errors.append(f"No payment via Business Cheque Account for {inv_id}")

    # Verify no overdue remain for Auckland contacts
    remaining = [i for i in invoices if i["status"] == "overdue" and i["contactId"] in auckland_ids]
    if remaining:
        nums = [i["invoiceNumber"] for i in remaining]
        errors.append(f"Still overdue for Auckland: {', '.join(nums)}")

    if errors:
        return False, "; ".join(errors)
    return True, f"All {len(target_ids)} overdue invoice(s) for Auckland contacts paid"
