import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find CN-0012 (CloudNine credit note)
    cn = next((c for c in state.get("creditNotes", []) if c.get("number") == "CN-0012"), None)
    if cn is None:
        return False, "Credit note CN-0012 not found."

    # Check CN-0012 has allocation to INV-0047
    allocations = cn.get("allocations", [])
    alloc_to_inv047 = next(
        (a for a in allocations if a.get("invoiceNumber") == "INV-0047" or a.get("invoiceId") == "inv_006"),
        None
    )
    if alloc_to_inv047 is None:
        return False, "CN-0012 has no allocation to INV-0047."

    if abs(alloc_to_inv047.get("amount", 0) - 2035.00) > 1.00:
        return False, f"Expected allocation amount ~$2,035, got ${alloc_to_inv047.get('amount', 0)}."

    # Check CN status is paid and remainingCredit ~0
    if cn.get("status") != "paid":
        return False, f"Expected CN-0012 status 'paid', got '{cn.get('status')}'."

    if abs(cn.get("remainingCredit", 9999)) > 1.00:
        return False, f"Expected CN-0012 remainingCredit ~0, got {cn.get('remainingCredit')}."

    # Check INV-0047 amountDue reduced by 2035
    inv = next((i for i in state.get("invoices", []) if i.get("number") == "INV-0047"), None)
    if inv is None:
        return False, "Invoice INV-0047 not found."

    expected_due = 18652.70 - 2035.00
    if abs(inv.get("amountDue", 0) - expected_due) > 1.00:
        return False, f"Expected INV-0047 amountDue ~${expected_due:.2f}, got ${inv.get('amountDue', 0)}."

    return True, "CN-0012 allocated to INV-0047 for $2,035 successfully."
