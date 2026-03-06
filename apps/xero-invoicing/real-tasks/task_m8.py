import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find CN-0009
    credit_notes = state.get("creditNotes", [])
    cn = None
    for c in credit_notes:
        if c.get("number") == "CN-0009":
            cn = c
            break

    if cn is None:
        return False, "Credit note CN-0009 not found."

    # Check CN-0009 has allocation to INV-0049
    allocations = cn.get("allocations", [])
    allocated_to_inv = False
    for a in allocations:
        if a.get("invoiceNumber") == "INV-0049" or a.get("invoiceId") == "inv_008":
            allocated_to_inv = True
            break

    if not allocated_to_inv:
        return False, f"CN-0009 has no allocation to INV-0049. Allocations: {allocations}"

    remaining = cn.get("remainingCredit", -1)
    if abs(remaining) > 0.01:
        return False, f"CN-0009 remainingCredit is {remaining}, expected approximately 0."

    # Check INV-0049 amountDue reduced
    invoices = state.get("invoices", [])
    inv = None
    for i in invoices:
        if i.get("number") == "INV-0049":
            inv = i
            break

    if inv is None:
        return False, "Invoice INV-0049 not found."

    # Original amountDue was 2996.00, should be reduced by 249.75
    expected_due = 2996.00 - 249.75
    actual_due = inv.get("amountDue", -1)
    if abs(actual_due - expected_due) > 1.00:
        return False, f"INV-0049 amountDue is {actual_due}, expected approximately {expected_due} (original 2996.00 minus 249.75)."

    return True, "CN-0009 allocated to INV-0049. remainingCredit=0, INV-0049 amountDue reduced by $249.75."
