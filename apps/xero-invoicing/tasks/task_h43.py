import requests


# Seed invoice IDs
SEED_INVOICE_IDS = {
    "inv_000", "inv_001", "inv_002", "inv_003", "inv_004", "inv_005",
    "inv_006", "inv_007", "inv_008", "inv_009", "inv_010", "inv_011",
    "inv_012", "inv_013", "inv_014", "inv_015", "inv_016", "inv_017",
    "inv_018", "inv_019", "inv_020", "inv_021", "inv_022", "inv_023",
    "inv_024", "inv_025",
}


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # QU-0024 (Atlas Engineering, $76,725) is the most expensive sent quote.
    # It should be accepted and invoiced.
    quo = None
    for q in state.get("quotes", []):
        if q.get("number") == "QU-0024":
            quo = q
            break

    if quo is None:
        return False, "Quote QU-0024 not found."

    if quo.get("status") != "accepted":
        return False, f"QU-0024 status is '{quo.get('status')}', expected 'accepted'."

    if not quo.get("isInvoiced"):
        return False, "QU-0024 is not marked as invoiced."

    # Find the new invoice for Atlas Engineering (con_025)
    new_inv = None
    for inv in state.get("invoices", []):
        if inv.get("contactId") == "con_025" and inv.get("id") not in SEED_INVOICE_IDS:
            new_inv = inv
            break

    if new_inv is None:
        return False, "No new invoice found for Atlas Engineering Consultants (con_025)."

    if new_inv.get("status") != "awaiting_payment":
        return False, (
            f"New invoice '{new_inv.get('number')}' status is '{new_inv.get('status')}', "
            f"expected 'awaiting_payment' (approved)."
        )

    if not new_inv.get("sentAt"):
        return False, f"New invoice '{new_inv.get('number')}' has not been sent."

    return True, (
        f"QU-0024 accepted and invoiced. New invoice '{new_inv.get('number')}' "
        f"for Atlas Engineering approved and sent."
    )
