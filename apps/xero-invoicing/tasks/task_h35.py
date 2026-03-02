import requests


# Seed credit note IDs
SEED_CN_IDS = {"cn_001", "cn_002", "cn_003", "cn_004", "cn_005"}


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # CloudNine Analytics = con_007
    # Smaller invoice = INV-0062 ($2,139.50) vs INV-0047 ($18,652.70)
    new_cn = None
    for cn in state.get("creditNotes", []):
        if cn.get("contactId") == "con_007" and cn.get("id") not in SEED_CN_IDS:
            new_cn = cn
            break

    if new_cn is None:
        return False, "No new credit note found for CloudNine Analytics (con_007)."

    # Should be approved (not draft)
    if new_cn.get("status") == "draft":
        return False, f"New credit note '{new_cn.get('number')}' is still draft — not approved."

    # Check line item: 5 hours dev at ~$185
    line_items = new_cn.get("lineItems", [])
    found = False
    for li in line_items:
        price = float(li.get("unitPrice", 0))
        qty = li.get("quantity", 0)
        if abs(price - 185.00) < 5.00 and qty == 5:
            found = True
            break

    if not found:
        items = [(li.get("unitPrice"), li.get("quantity")) for li in line_items]
        return False, (
            f"No line item with qty 5 and unitPrice ~$185 (development) found. Items: {items}."
        )

    # Check it was allocated to INV-0062 (the smaller invoice)
    allocations = new_cn.get("allocations", [])
    alloc_to_smaller = None
    for alloc in allocations:
        if alloc.get("invoiceNumber") == "INV-0062":
            alloc_to_smaller = alloc
            break

    if alloc_to_smaller is None:
        alloc_targets = [a.get("invoiceNumber") for a in allocations]
        return False, (
            f"Credit note not allocated to INV-0062 (the smaller CloudNine invoice). "
            f"Allocations target: {alloc_targets}."
        )

    return True, (
        f"Credit note '{new_cn.get('number')}' created for CloudNine Analytics "
        f"(5 hrs dev at $185), approved, and allocated against INV-0062 (the smaller invoice)."
    )
