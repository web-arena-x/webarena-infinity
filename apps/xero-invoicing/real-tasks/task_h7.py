import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    invoice = next((inv for inv in state.get("invoices", []) if inv.get("number") == "INV-0052"), None)
    if invoice is None:
        return False, "Invoice INV-0052 not found."

    # Check payment of ~$5,000
    payments = invoice.get("payments", [])
    payment_5k = next((p for p in payments if abs(p.get("amount", 0) - 5000.00) < 1.00), None)
    if payment_5k is None:
        return False, "No payment of ~$5,000 found on INV-0052."

    # Check amountDue ~22324 (27324 - 5000)
    expected_due = 27324.00 - 5000.00
    if abs(invoice.get("amountDue", 0) - expected_due) > 1.00:
        return False, f"Expected amountDue ~${expected_due:.2f}, got ${invoice.get('amountDue', 0)}."

    # Check title
    if invoice.get("title") != "March 2026 Development Sprint":
        return False, f"Expected title 'March 2026 Development Sprint', got '{invoice.get('title')}'."

    return True, "INV-0052: $5,000 partial payment recorded and title set to 'March 2026 Development Sprint'."
