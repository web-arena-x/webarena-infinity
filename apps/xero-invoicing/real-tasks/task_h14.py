import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    invoice = next((inv for inv in state.get("invoices", []) if inv.get("number") == "INV-0057"), None)
    if invoice is None:
        return False, "Invoice INV-0057 not found."

    if invoice.get("status") != "paid":
        return False, f"Expected INV-0057 status 'paid', got '{invoice.get('status')}'."

    if abs(invoice.get("amountDue", 9999)) > 0.01:
        return False, f"Expected amountDue=0, got {invoice.get('amountDue')}."

    if not invoice.get("sentAt"):
        return False, "INV-0057 has not been sent (sentAt is null)."

    # Check has payment ~6600
    payments = invoice.get("payments", [])
    payment_6600 = next((p for p in payments if abs(p.get("amount", 0) - 6600.00) < 1.00), None)
    if payment_6600 is None:
        return False, "No payment of ~$6,600 found on INV-0057."

    return True, "INV-0057 (Stellar Education) approved, sent, and fully paid ($6,600)."
