"""Verify: Full payment on oldest overdue invoice (inv_87) via Business Savings Account."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    state = requests.get(f"{server_url}/api/state", timeout=5).json()
    invoices = state.get("invoices", [])
    payments = state.get("payments", [])

    # inv_87 (INV-0087) is the oldest overdue by issue date (2025-10-13)
    inv = next((i for i in invoices if i["id"] == "inv_87"), None)
    if not inv:
        return False, "Invoice inv_87 not found"

    errors = []

    if inv["status"] != "paid":
        errors.append(f"Invoice status is '{inv['status']}', expected 'paid'")

    if abs(inv["amountDue"]) > 0.01:
        errors.append(f"amountDue is {inv['amountDue']}, expected 0")

    # Check payment via Business Savings (bank_2)
    inv_payments = [p for p in payments if p["invoiceId"] == "inv_87"]
    savings_payments = [p for p in inv_payments if p.get("bankAccountId") == "bank_2"]
    if not savings_payments:
        errors.append("No payment found via Business Savings Account (bank_2)")

    if errors:
        return False, "; ".join(errors)
    return True, "Full payment recorded on oldest overdue invoice (INV-0087) via Business Savings Account"
