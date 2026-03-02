import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # INV-0045 (Pinnacle Construction Group) had a partial payment of $4,950.
    # The task requires removing that payment, then voiding the invoice.
    inv = None
    for i in state.get("invoices", []):
        if i.get("number") == "INV-0045":
            inv = i
            break

    if inv is None:
        return False, "Invoice INV-0045 not found."

    status = inv.get("status", "")
    if status != "voided":
        return False, f"INV-0045 status is '{status}', expected 'voided'."

    amount_due = float(inv.get("amountDue", -1))
    if amount_due != 0:
        return False, f"INV-0045 amountDue is ${amount_due:.2f}, expected $0 (voided)."

    payments = inv.get("payments", [])
    if len(payments) > 0:
        return False, (
            f"INV-0045 still has {len(payments)} payment(s). "
            f"The partial payment should have been removed before voiding."
        )

    return True, (
        "INV-0045 (Pinnacle Construction) partial payment removed and invoice voided."
    )
