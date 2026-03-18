import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Delete all draft invoices for Metro Print Solutions and Apex Legal Partners."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    invoices = state.get("invoices", [])

    # Specific draft invoices that should be deleted
    deleted_ids = {"inv_83", "inv_108", "inv_93"}

    errors = []

    # Check that none of the specific draft invoices exist
    for inv in invoices:
        if inv.get("id") in deleted_ids:
            errors.append(
                f"Invoice {inv.get('invoiceNumber', inv.get('id'))} ({inv.get('id')}) still exists, expected deleted"
            )

    # Also verify no draft invoice exists for con_8 or con_18
    for inv in invoices:
        if inv.get("contactId") in ("con_8", "con_18") and inv.get("status") == "draft":
            errors.append(
                f"Draft invoice {inv.get('invoiceNumber', inv.get('id'))} ({inv.get('id')}) "
                f"still exists for contact {inv.get('contactId')}"
            )

    if errors:
        return False, "; ".join(errors)

    return True, "All draft invoices for Metro Print Solutions (inv_83, inv_108) and Apex Legal Partners (inv_93) deleted"
