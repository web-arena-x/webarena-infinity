import requests


SEED_CN_IDS = {"cn_001", "cn_002", "cn_003", "cn_004", "cn_005"}


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # New credit note for Coastal Living Interiors (con_011):
    # 2x Widget A at ~$24.95, approved, allocated against INV-0049.
    new_cn = None
    for cn in state.get("creditNotes", []):
        if cn.get("contactId") == "con_011" and cn.get("id") not in SEED_CN_IDS:
            new_cn = cn
            break

    if new_cn is None:
        return False, "No new credit note found for Coastal Living Interiors (con_011)."

    # Should be approved (not draft)
    if new_cn.get("status") == "draft":
        return False, (
            f"New credit note '{new_cn.get('number')}' is still draft — not approved."
        )

    # Check line item: 2x Widget A at ~$24.95
    line_items = new_cn.get("lineItems", [])
    found = False
    for li in line_items:
        price = float(li.get("unitPrice", 0))
        qty = li.get("quantity", 0)
        if abs(price - 24.95) < 3.00 and qty == 2:
            found = True
            break

    if not found:
        items = [(li.get("unitPrice"), li.get("quantity")) for li in line_items]
        return False, (
            f"No line item with qty 2 and unitPrice ~$24.95 (Widget A) found. Items: {items}."
        )

    # Check allocation to INV-0049
    allocations = new_cn.get("allocations", [])
    alloc_to_inv49 = None
    for alloc in allocations:
        if alloc.get("invoiceNumber") == "INV-0049":
            alloc_to_inv49 = alloc
            break

    if alloc_to_inv49 is None:
        alloc_targets = [a.get("invoiceNumber") for a in allocations]
        return False, (
            f"Credit note not allocated to INV-0049. Allocations: {alloc_targets}."
        )

    return True, (
        f"Credit note '{new_cn.get('number')}' created for Coastal Living Interiors "
        f"(2x Widget A), approved, and allocated against INV-0049."
    )
