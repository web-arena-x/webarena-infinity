import requests


# Seed repeating invoice IDs
SEED_REPEAT_IDS = {"rep_001", "rep_002", "rep_003", "rep_004", "rep_005"}


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Outback Adventures Tourism = con_015
    new_ri = None
    for ri in state.get("repeatingInvoices", []):
        if ri.get("contactId") == "con_015" and ri.get("id") not in SEED_REPEAT_IDS:
            new_ri = ri
            break

    if new_ri is None:
        return False, "No new repeating invoice found for Outback Adventures Tourism (con_015)."

    freq = new_ri.get("frequency", "")
    if freq != "fortnightly":
        return False, f"Repeating invoice frequency is '{freq}', expected 'fortnightly'."

    save_as = new_ri.get("saveAs", "")
    if save_as != "approved":
        return False, f"Repeating invoice saveAs is '{save_as}', expected 'approved'."

    start = new_ri.get("startDate", "")
    if not start.startswith("2026-05"):
        return False, f"Repeating invoice startDate is '{start}', expected May 2026."

    line_items = new_ri.get("lineItems", [])
    if len(line_items) < 1:
        return False, "Repeating invoice has no line items."

    found = False
    for li in line_items:
        price = float(li.get("unitPrice", 0))
        qty = li.get("quantity", 0)
        if abs(price - 165.00) < 5.00 and qty == 3:
            found = True
            break

    if not found:
        items = [(li.get("unitPrice"), li.get("quantity")) for li in line_items]
        return False, f"No line item with qty 3 and unitPrice ~$165 (UI/UX design) found. Items: {items}."

    return True, (
        "Fortnightly repeating invoice created for Outback Adventures Tourism: "
        "3 hours UI/UX design at $165/hr, starting May 2026, saved as approved."
    )
