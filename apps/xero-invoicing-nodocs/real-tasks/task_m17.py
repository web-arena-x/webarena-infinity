import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Approve all invoices currently awaiting approval from Hamilton Plumbing Services."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    invoices = state.get("invoices", [])

    # Find invoice INV-0077 (inv_77) which was the awaiting_approval invoice for Hamilton Plumbing
    target = None
    for inv in invoices:
        if inv.get("id") == "inv_77" or inv.get("invoiceNumber") == "INV-0077":
            target = inv
            break

    if target is None:
        return False, "Invoice INV-0077 not found in state"

    status = target.get("status")
    if status != "awaiting_payment":
        return False, f"Invoice INV-0077 has status '{status}', expected 'awaiting_payment' (approved)"

    # Also verify no invoices for Hamilton Plumbing (con_2) remain in awaiting_approval
    still_awaiting = []
    for inv in invoices:
        if inv.get("contactId") == "con_2" and inv.get("status") == "awaiting_approval":
            still_awaiting.append(inv.get("invoiceNumber", inv.get("id")))

    if still_awaiting:
        return False, f"Hamilton Plumbing Services still has invoices awaiting approval: {still_awaiting}"

    return True, "All Hamilton Plumbing Services invoices have been approved; INV-0077 is now awaiting payment"
