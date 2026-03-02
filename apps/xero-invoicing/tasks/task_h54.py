import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    reminders = state.get("invoiceReminders", [])

    target = None
    for r in reminders:
        if r.get("timing") == "after" and r.get("days") == 45:
            target = r
            break

    if target is None:
        existing = [(r.get("timing"), r.get("days")) for r in reminders]
        return False, (
            f"No invoice reminder found for 45 days after the due date. "
            f"Existing reminders: {existing}."
        )

    expected_subject = "Final notice: Invoice {InvoiceNumber} - Account referred to collections"
    subject = target.get("subject", "")
    if subject != expected_subject:
        return False, f"Reminder subject is '{subject}', expected '{expected_subject}'."

    if not target.get("includeInvoicePdf"):
        return False, "Reminder does not include the invoice PDF."

    if target.get("includeSummary") is not False:
        return False, (
            f"Reminder includeSummary is {target.get('includeSummary')}, expected False."
        )

    if not target.get("enabled"):
        return False, "Reminder is not enabled."

    return True, (
        "Invoice reminder created: 45 days after due date, correct subject, "
        "PDF included, summary excluded, enabled."
    )
