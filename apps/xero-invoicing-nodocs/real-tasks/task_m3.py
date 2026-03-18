import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Copy invoice INV-0009 for Pinnacle Construction Co and save the copy as a draft."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    invoices = state.get("invoices", [])

    # Count invoices for Pinnacle Construction Co (con_9)
    con_9_invoices = [inv for inv in invoices if inv.get("contactId") == "con_9"]

    # The original data should have some invoices for con_9; after copying INV-0009 there should be more
    # We need at least one NEW draft invoice for con_9 that is not inv_9 itself
    original_inv = None
    new_drafts = []
    for inv in con_9_invoices:
        if inv.get("id") == "inv_9" or inv.get("invoiceNumber") == "INV-0009":
            original_inv = inv
        elif inv.get("status") == "draft":
            new_drafts.append(inv)

    if original_inv is None:
        return False, "Original invoice INV-0009 not found in state"

    if not new_drafts:
        # Also check if there are any new invoices (non-original) for con_9 regardless of status
        all_new = [inv for inv in con_9_invoices if inv.get("id") != "inv_9" and inv.get("invoiceNumber") != "INV-0009"]
        if not all_new:
            return False, "No new invoice found for Pinnacle Construction Co (con_9). Expected a copy of INV-0009."
        # There are new invoices but none are drafts
        statuses = [inv.get("status") for inv in all_new]
        return False, f"New invoice(s) found for con_9 but none are drafts. Statuses: {statuses}"

    # Verify the copy has the same contactId
    copy = new_drafts[0]
    if copy.get("contactId") != "con_9":
        return False, f"Copy invoice contactId is '{copy.get('contactId')}', expected 'con_9'"

    return True, f"Found a new draft invoice (id={copy.get('id')}) for Pinnacle Construction Co that copies INV-0009"
