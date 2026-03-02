import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # rep_001 (Greenfield Organics) and rep_003 (Cascade Software Solutions) are the
    # repeating invoices set to 'approved_for_sending'. Both should be changed to 'draft'.
    expected_changes = {
        "rep_001": "Greenfield Organics",
        "rep_003": "Cascade Software Solutions",
    }

    for rep_id, contact_name in expected_changes.items():
        ri = None
        for r in state.get("repeatingInvoices", []):
            if r.get("id") == rep_id:
                ri = r
                break

        if ri is None:
            return False, f"Repeating invoice {rep_id} ({contact_name}) not found."

        save_as = ri.get("saveAs", "")
        if save_as != "draft":
            return False, (
                f"Repeating invoice {rep_id} ({contact_name}) saveAs is '{save_as}', "
                f"expected 'draft'."
            )

    # Verify that other repeating invoices were NOT changed
    # rep_002 (CloudNine) was already 'draft', rep_004 (Vanguard) was 'approved',
    # rep_005 (Summit Health) was 'draft' — none should change
    for r in state.get("repeatingInvoices", []):
        rid = r.get("id")
        if rid == "rep_004" and r.get("saveAs") != "approved":
            return False, (
                f"rep_004 (Vanguard Security) saveAs was changed to '{r.get('saveAs')}', "
                f"but it was 'approved', not 'approved_for_sending' — should not have been touched."
            )

    return True, (
        "Both auto-send repeating invoices (rep_001 Greenfield, rep_003 Cascade) "
        "changed from 'approved_for_sending' to 'draft'."
    )
