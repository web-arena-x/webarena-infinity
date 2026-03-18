import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Delete all draft invoices that are in AUD."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    invoices = state.get("invoices", [])

    # The specific AUD draft invoices that should have been deleted
    deleted_ids = {"inv_18", "inv_25", "inv_61"}

    errors = []

    # Check that none of the specific invoices exist
    for inv in invoices:
        if inv.get("id") in deleted_ids:
            errors.append(
                f"Invoice {inv.get('id')} ({inv.get('invoiceNumber')}) still exists in state but should have been deleted"
            )

    # Also check that no draft AUD invoices exist at all
    remaining_aud_drafts = []
    for inv in invoices:
        if inv.get("status") == "draft" and inv.get("currency") == "AUD":
            remaining_aud_drafts.append(
                f"{inv.get('id')} ({inv.get('invoiceNumber')})"
            )

    if remaining_aud_drafts:
        errors.append(
            f"Draft AUD invoices still exist: {', '.join(remaining_aud_drafts)}"
        )

    if errors:
        return False, "; ".join(errors)

    return True, "All draft AUD invoices (inv_18, inv_25, inv_61) have been deleted"
