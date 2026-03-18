import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Approve and send all invoices that are currently awaiting approval and denominated in NZD."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    invoices = state.get("invoices", [])

    # The NZD awaiting_approval invoices that should be approved and sent
    target_ids = {"inv_8", "inv_17", "inv_38", "inv_56", "inv_66", "inv_77", "inv_111"}

    errors = []

    for inv_id in target_ids:
        inv = None
        for i in invoices:
            if i.get("id") == inv_id:
                inv = i
                break

        if inv is None:
            errors.append(f"Invoice {inv_id} not found in state")
            continue

        status = inv.get("status")
        if status != "awaiting_payment":
            errors.append(
                f"Invoice {inv_id} ({inv.get('invoiceNumber')}) has status '{status}', expected 'awaiting_payment'"
            )

        sent_at = inv.get("sentAt")
        if sent_at is None:
            errors.append(
                f"Invoice {inv_id} ({inv.get('invoiceNumber')}) has sentAt=None, expected a timestamp"
            )

    # Also verify no NZD invoices remain in awaiting_approval status
    remaining = []
    for inv in invoices:
        if inv.get("currency") == "NZD" and inv.get("status") == "awaiting_approval":
            remaining.append(f"{inv.get('id')} ({inv.get('invoiceNumber')})")

    if remaining:
        errors.append(
            f"NZD invoices still awaiting approval: {', '.join(remaining)}"
        )

    if errors:
        return False, "; ".join(errors)

    return True, "All 7 NZD awaiting-approval invoices have been approved (awaiting_payment) and sent"
