import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find Greenfield Organics contact
    contacts = state.get("contacts", [])
    greenfield_id = None
    for c in contacts:
        if "greenfield" in c.get("name", "").lower():
            greenfield_id = c.get("id")
            break

    if greenfield_id is None:
        return False, "Greenfield Organics contact not found in state."

    credit_notes = state.get("creditNotes", [])
    matching_cn = None
    for cn in credit_notes:
        if cn.get("contactId") != greenfield_id:
            continue
        # Check if this is a new credit note (not an existing one)
        line_items = cn.get("lineItems", [])
        for li in line_items:
            desc = li.get("description", "").lower()
            price = li.get("unitPrice", 0)
            total = cn.get("total", 0)
            # Check for hosting/credit mention or price around 200
            if abs(price - 200.00) < 1.00 or (total >= 200 and total <= 220):
                matching_cn = cn
                break
            if ("hosting" in desc or "credit" in desc) and total > 0:
                matching_cn = cn
                break
        if matching_cn:
            break

    if matching_cn is None:
        return False, "No credit note found for Greenfield Organics with ~$200 hosting credit."

    return True, f"Credit note {matching_cn.get('number')} created for Greenfield Organics for hosting credit."
