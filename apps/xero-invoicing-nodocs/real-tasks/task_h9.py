import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Copy invoice INV-0001, change contact on copy to Meridian Health Clinic, save as draft."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    invoices = state.get("invoices", [])

    errors = []

    # Check original INV-0001 still exists and is unchanged
    original = None
    for inv in invoices:
        if inv.get("id") == "inv_1":
            original = inv
            break

    if original is None:
        errors.append("Original invoice inv_1 (INV-0001) not found - it should still exist")
    else:
        if original.get("contactId") != "con_1":
            errors.append(
                f"Original INV-0001 contactId changed to '{original.get('contactId')}', "
                "should still be 'con_1' (Ridgeway University)"
            )
        if original.get("status") != "paid":
            errors.append(
                f"Original INV-0001 status changed to '{original.get('status')}', should still be 'paid'"
            )

    # Check that there's a new draft invoice for Meridian Health Clinic (con_22)
    meridian_invoices = [inv for inv in invoices if inv.get("contactId") == "con_22"]

    # Originally con_22 has 4 invoices; after copying there should be more
    if len(meridian_invoices) <= 4:
        errors.append(
            f"Found {len(meridian_invoices)} invoices for Meridian Health Clinic (con_22), "
            "expected more than 4 (original count) after copying INV-0001"
        )

    # Find a draft invoice for con_22 that could be the copy
    draft_meridian = [inv for inv in meridian_invoices if inv.get("status") == "draft"]
    if not draft_meridian:
        errors.append(
            "No draft invoice found for Meridian Health Clinic (con_22) - the copy should be saved as draft"
        )

    if errors:
        return False, "; ".join(errors)

    return True, "INV-0001 copied to Meridian Health Clinic as draft; original unchanged"
