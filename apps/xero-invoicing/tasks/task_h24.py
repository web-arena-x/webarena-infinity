import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # CN-0011 (Pacific Freight Lines, con_006) — approve then allocate to INV-0048
    cn = None
    for c in state.get("creditNotes", []):
        if c.get("number") == "CN-0011":
            cn = c
            break

    if cn is None:
        return False, "Credit note CN-0011 not found."

    # Must not be draft (should be approved → allocated → paid)
    if cn.get("status") == "draft":
        return False, "CN-0011 is still in draft status — it has not been approved."

    # Check it has allocations
    allocations = cn.get("allocations", [])
    if len(allocations) < 1:
        return False, "CN-0011 has no allocations."

    # Check allocation targets INV-0048
    target_alloc = None
    for alloc in allocations:
        if alloc.get("invoiceNumber") == "INV-0048":
            target_alloc = alloc
            break

    if target_alloc is None:
        alloc_invoices = [a.get("invoiceNumber") for a in allocations]
        return False, (
            f"No allocation found for INV-0048. "
            f"Allocations target: {alloc_invoices}."
        )

    # Check allocation amount is approximately $968
    alloc_amount = float(target_alloc.get("amount", 0))
    if abs(alloc_amount - 968.00) > 5.00:
        return False, f"Allocation amount is ${alloc_amount:.2f}, expected ~$968.00."

    # Check remaining credit is approximately 0
    remaining = float(cn.get("remainingCredit", 9999))
    if remaining > 1.00:
        return False, f"CN-0011 remainingCredit is ${remaining:.2f}, expected ~$0."

    return True, (
        "Credit note CN-0011 ($968) approved and fully allocated against INV-0048 "
        "(Pacific Freight Lines)."
    )
