import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Mark the Bright Spark Electrical draft invoice as approved."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    invoices = state.get("invoices", [])
    contacts = state.get("contacts", [])

    # Find the contact for Bright Spark Electrical
    bright_spark_id = None
    for contact in contacts:
        if contact.get("name") == "Bright Spark Electrical":
            bright_spark_id = contact.get("id")
            break

    if bright_spark_id is None:
        return False, "Contact 'Bright Spark Electrical' not found"

    # Find the invoice for this contact (expected INV-0005)
    target = None
    for inv in invoices:
        if inv.get("contactId") == bright_spark_id:
            target = inv
            break

    if target is None:
        return False, f"No invoice found for contact 'Bright Spark Electrical' (id: {bright_spark_id})"

    status = target.get("status")
    if status == "awaiting_payment":
        return True, f"Invoice {target.get('invoiceNumber')} for Bright Spark Electrical has been approved (status: awaiting_payment)"
    else:
        return False, f"Invoice {target.get('invoiceNumber')} for Bright Spark Electrical has status '{status}', expected 'awaiting_payment'"
