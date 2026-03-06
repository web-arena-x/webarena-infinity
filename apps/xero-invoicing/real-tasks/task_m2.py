import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    invoices = state.get("invoices", [])

    # Find original INV-0046
    original = None
    for i in invoices:
        if i.get("number") == "INV-0046":
            original = i
            break

    if original is None:
        return False, "Original invoice INV-0046 not found."

    original_contact = original.get("contactId")

    # Look for a new draft invoice with the same contactId
    new_draft = None
    for i in invoices:
        if i.get("number") == "INV-0046":
            continue
        if i.get("status") == "draft" and i.get("contactId") == original_contact:
            # Check total is approximately the same as INV-0046
            total = i.get("total", 0)
            if abs(total - 6655.00) < 1.00:
                new_draft = i
                break

    if new_draft is None:
        # Broader search: any new draft for same contact
        for i in invoices:
            if i.get("number") == "INV-0046":
                continue
            if i.get("status") == "draft" and i.get("contactId") == original_contact:
                new_draft = i
                break

    if new_draft is None:
        return False, f"No new draft invoice found for contact '{original_contact}' (Baxter & Associates)."

    new_total = new_draft.get("total", 0)
    if abs(new_total - 6655.00) < 1.00:
        return True, f"New draft invoice {new_draft.get('number')} created as copy of INV-0046 with total ${new_total}."

    return True, f"New draft invoice {new_draft.get('number')} created for same contact as INV-0046 (total=${new_total})."
