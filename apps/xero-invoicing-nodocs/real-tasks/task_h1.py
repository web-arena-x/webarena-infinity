import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Void all overdue invoices for Bloom & Branch Florists."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    invoices = state.get("invoices", [])

    target_ids = {"inv_15", "inv_40"}
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
        if status != "voided":
            errors.append(
                f"Invoice {inv_id} ({inv.get('invoiceNumber')}) has status '{status}', expected 'voided'"
            )

        voided_at = inv.get("voidedAt")
        if voided_at is None:
            errors.append(
                f"Invoice {inv_id} ({inv.get('invoiceNumber')}) has voidedAt=None, expected a timestamp"
            )

    if errors:
        return False, "; ".join(errors)

    return True, "All overdue invoices for Bloom & Branch Florists (inv_15, inv_40) have been voided"
