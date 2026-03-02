import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # QU-0023 (Redback Mining Supplies) must be accepted and invoiced
    quo = None
    for q in state.get("quotes", []):
        if q.get("number") == "QU-0023":
            quo = q
            break

    if quo is None:
        return False, "Quote QU-0023 not found."

    if quo.get("status") != "accepted":
        return False, f"QU-0023 status is '{quo.get('status')}', expected 'accepted'."

    if not quo.get("isInvoiced"):
        return False, "QU-0023 has not been converted to an invoice (isInvoiced is False)."

    # Check that a new invoice exists for Redback Mining Supplies (con_010)
    seed_invoice_ids = {
        "inv_000", "inv_001", "inv_002", "inv_003", "inv_004", "inv_005",
        "inv_006", "inv_007", "inv_008", "inv_009", "inv_010", "inv_011",
        "inv_012", "inv_013", "inv_014", "inv_015", "inv_016", "inv_017",
        "inv_018", "inv_019", "inv_020", "inv_021", "inv_022", "inv_023",
        "inv_024", "inv_025",
    }
    new_inv = None
    for inv in state.get("invoices", []):
        if inv.get("contactId") == "con_010" and inv.get("id") not in seed_invoice_ids:
            new_inv = inv
            break

    if new_inv is None:
        return False, "No new invoice found for Redback Mining Supplies (con_010)."

    return True, (
        f"Quote QU-0023 accepted and converted to invoice '{new_inv.get('number')}' "
        f"for Redback Mining Supplies."
    )
