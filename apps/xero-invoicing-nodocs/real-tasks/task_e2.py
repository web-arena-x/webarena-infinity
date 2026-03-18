import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Void the overdue invoice sent to Bloom & Branch Florists for $35,937.50."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    invoices = state.get("invoices", [])
    contacts = state.get("contacts", [])

    # Find the contact for Bloom & Branch Florists
    bloom_contact_id = None
    for contact in contacts:
        if contact.get("name") == "Bloom & Branch Florists":
            bloom_contact_id = contact.get("id")
            break

    if bloom_contact_id is None:
        return False, "Contact 'Bloom & Branch Florists' not found"

    # Find the matching invoice
    target = None
    for inv in invoices:
        if (inv.get("contactId") == bloom_contact_id
                and inv.get("total") == 35937.5):
            target = inv
            break

    if target is None:
        # Also try matching by invoice number as fallback
        for inv in invoices:
            if inv.get("invoiceNumber") == "INV-0015":
                target = inv
                break

    if target is None:
        return False, "Could not find the overdue invoice for Bloom & Branch Florists with total $35,937.50"

    status = target.get("status")
    voided_at = target.get("voidedAt")

    errors = []
    if status != "voided":
        errors.append(f"status is '{status}', expected 'voided'")
    if not voided_at:
        errors.append("voidedAt is null or missing, expected a timestamp")

    if errors:
        return False, f"Invoice {target.get('invoiceNumber')}: {'; '.join(errors)}"

    return True, f"Invoice {target.get('invoiceNumber')} for Bloom & Branch Florists has been voided successfully"
