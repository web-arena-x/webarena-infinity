import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Record the remaining balance on all partially-paid invoices using the Business Cheque Account."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    invoices = state.get("invoices", [])
    payments = state.get("payments", [])

    # Partially-paid invoices and their expected remaining balances
    targets = {
        "inv_6": 4875.84,
        "inv_34": 2388.96,
        "inv_55": 37.20,
        "inv_74": 802.82,
    }

    errors = []

    for inv_id, expected_due in targets.items():
        inv = None
        for i in invoices:
            if i.get("id") == inv_id:
                inv = i
                break

        if inv is None:
            errors.append(f"Invoice {inv_id} not found in state")
            continue

        inv_num = inv.get("invoiceNumber", inv_id)

        status = inv.get("status")
        if status != "paid":
            errors.append(f"Invoice {inv_num} ({inv_id}) has status '{status}', expected 'paid'")

        amount_due = inv.get("amountDue", 0)
        if abs(amount_due) > 0.01:
            errors.append(f"Invoice {inv_num} ({inv_id}) has amountDue={amount_due}, expected ~0")

        # Check that a new payment exists for this invoice with bankAccountId == 'bank_1'
        found_payment = False
        for p in payments:
            if p.get("invoiceId") == inv_id and p.get("bankAccountId") == "bank_1":
                if abs(p.get("amount", 0) - expected_due) < 0.01:
                    found_payment = True
                    break

        if not found_payment:
            errors.append(
                f"No payment found for {inv_num} ({inv_id}) with amount ~{expected_due} and bankAccountId='bank_1'"
            )

    if errors:
        return False, "; ".join(errors)

    return True, "All 4 partially-paid invoices (inv_6, inv_34, inv_55, inv_74) are now fully paid via Business Cheque Account"
