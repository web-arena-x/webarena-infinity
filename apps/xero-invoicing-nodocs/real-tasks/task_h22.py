"""Verify: Partial payment of half the max-total overdue invoice (inv_40, $121,725)."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    state = requests.get(f"{server_url}/api/state", timeout=5).json()
    invoices = state.get("invoices", [])
    payments = state.get("payments", [])

    inv = next((i for i in invoices if i["id"] == "inv_40"), None)
    if not inv:
        return False, "Invoice inv_40 not found"

    expected_payment = 60862.50
    errors = []

    # Check amountPaid
    if abs(inv["amountPaid"] - expected_payment) > 0.01:
        errors.append(f"amountPaid is {inv['amountPaid']}, expected {expected_payment}")

    # Should NOT be fully paid
    if inv["status"] == "paid":
        errors.append("Invoice should not be fully paid (only half was due)")

    # Check payment exists
    inv_payments = [p for p in payments if p["invoiceId"] == "inv_40"]
    matching = [p for p in inv_payments if abs(p["amount"] - expected_payment) < 0.01]
    if not matching:
        errors.append(f"No payment of ${expected_payment:.2f} found for inv_40")
    elif matching[0].get("bankAccountId") != "bank_1":
        errors.append(f"Payment bankAccountId is '{matching[0].get('bankAccountId')}', expected 'bank_1'")

    if errors:
        return False, "; ".join(errors)
    return True, f"Half payment of ${expected_payment:.2f} recorded on inv_40 (highest-total overdue)"
