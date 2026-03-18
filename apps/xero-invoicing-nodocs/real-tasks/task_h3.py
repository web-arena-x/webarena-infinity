import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Record full payments for all overdue invoices from Nexus Technologies Ltd using the Business Cheque Account."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    invoices = state.get("invoices", [])
    payments = state.get("payments", [])

    target_invoices = {
        "inv_79": {"number": "INV-0079", "original_due": 6603.88},
        "inv_104": {"number": "INV-0104", "original_due": 7038},
    }

    errors = []

    for inv_id, info in target_invoices.items():
        inv = None
        for i in invoices:
            if i.get("id") == inv_id:
                inv = i
                break

        if inv is None:
            errors.append(f"Invoice {inv_id} ({info['number']}) not found in state")
            continue

        status = inv.get("status")
        if status != "paid":
            errors.append(
                f"Invoice {inv_id} ({info['number']}) has status '{status}', expected 'paid'"
            )

        amount_due = inv.get("amountDue", 0)
        if amount_due is None:
            amount_due = 0
        if amount_due > 0.01:
            errors.append(
                f"Invoice {inv_id} ({info['number']}) has amountDue={amount_due}, expected 0"
            )

        # Check that a payment exists for this invoice with correct bank account
        inv_payments = [p for p in payments if p.get("invoiceId") == inv_id]
        if not inv_payments:
            errors.append(
                f"No payment found for invoice {inv_id} ({info['number']})"
            )
        else:
            has_correct_bank = False
            for p in inv_payments:
                if p.get("bankAccountId") == "bank_1":
                    has_correct_bank = True
                    break
            if not has_correct_bank:
                errors.append(
                    f"Payment for {inv_id} ({info['number']}) does not use bankAccountId='bank_1' (Business Cheque Account)"
                )

    if errors:
        return False, "; ".join(errors)

    return True, "Both overdue invoices for Nexus Technologies Ltd (inv_79, inv_104) are fully paid via Business Cheque Account"
