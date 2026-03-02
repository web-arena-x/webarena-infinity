import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Overdue invoices (awaiting_payment, dueDate < 2026-03-02) with no prior payments:
    # INV-0046 (Baxter, due 2026-02-01, $6,655)
    # INV-0047 (CloudNine, due 2026-02-15, $18,652.70)
    # INV-0049 (Coastal Living, due 2026-02-24, $3,715)
    # INV-0051 (Summit Health, due 2026-03-01, $6,060)
    #
    # INV-0045 (Pinnacle, due 2026-02-19) is overdue but has a partial payment — excluded.

    expected = {
        "INV-0046": 6655.00,
        "INV-0047": 18652.70,
        "INV-0049": 3715.00,
        "INV-0051": 6060.00,
    }

    for inv_num, orig_due in expected.items():
        inv = None
        for i in state.get("invoices", []):
            if i.get("number") == inv_num:
                inv = i
                break

        if inv is None:
            return False, f"Invoice {inv_num} not found."

        if inv.get("status") != "paid":
            return False, (
                f"{inv_num} status is '{inv.get('status')}', expected 'paid'."
            )

        amount_due = float(inv.get("amountDue", 9999))
        if amount_due > 1.00:
            return False, (
                f"{inv_num} amountDue is ${amount_due:.2f}, expected ~$0."
            )

    # Verify INV-0045 was NOT paid (it had a prior partial payment, so should be excluded)
    for i in state.get("invoices", []):
        if i.get("number") == "INV-0045":
            if i.get("status") == "paid":
                return False, (
                    "INV-0045 was also paid, but it already had a partial payment "
                    "and should have been excluded."
                )
            break

    return True, (
        "All overdue invoices with no prior payments (INV-0046, INV-0047, INV-0049, INV-0051) "
        "have been fully paid."
    )
