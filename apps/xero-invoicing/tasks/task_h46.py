import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # CN-0012 (CloudNine Analytics, $2,035 remaining credit) should be allocated to
    # INV-0047 (due 2026-02-15), which is the soonest-due of CloudNine's two open invoices
    # (the other is INV-0062, due 2026-03-06).
    cn = None
    for c in state.get("creditNotes", []):
        if c.get("number") == "CN-0012":
            cn = c
            break

    if cn is None:
        return False, "Credit note CN-0012 not found."

    allocations = cn.get("allocations", [])
    alloc_to_inv47 = None
    for alloc in allocations:
        if alloc.get("invoiceNumber") == "INV-0047":
            alloc_to_inv47 = alloc
            break

    if alloc_to_inv47 is None:
        alloc_targets = [a.get("invoiceNumber") for a in allocations]
        return False, (
            f"CN-0012 not allocated to INV-0047 (soonest-due CloudNine invoice). "
            f"Allocations: {alloc_targets}."
        )

    alloc_amount = float(alloc_to_inv47.get("amount", 0))
    if alloc_amount < 100:
        return False, f"Allocation amount to INV-0047 is ${alloc_amount:.2f}, expected significant amount."

    return True, (
        f"CN-0012 allocated ${alloc_amount:.2f} to INV-0047 "
        f"(CloudNine's soonest-due invoice, due 2026-02-15)."
    )
