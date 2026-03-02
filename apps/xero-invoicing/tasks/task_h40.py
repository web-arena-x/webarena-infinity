import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    reminders = state.get("invoiceReminders", [])

    # Find a reminder with timing=before, days=3
    target = None
    for r in reminders:
        if r.get("timing") == "before" and r.get("days") == 3:
            target = r
            break

    if target is None:
        before_reminders = [(r.get("timing"), r.get("days")) for r in reminders]
        return False, (
            f"No invoice reminder found for 3 days before the due date. "
            f"Existing reminders: {before_reminders}."
        )

    expected_subject = "Friendly reminder: Invoice {InvoiceNumber} due in 3 days"
    subject = target.get("subject", "")
    if subject != expected_subject:
        return False, f"Reminder subject is '{subject}', expected '{expected_subject}'."

    if not target.get("includeInvoicePdf"):
        return False, "Reminder does not include the invoice PDF."

    if not target.get("includeSummary"):
        return False, "Reminder does not include the detail summary."

    if not target.get("enabled"):
        return False, "Reminder is not enabled."

    return True, (
        "Invoice reminder created: 3 days before due date, correct subject, "
        "PDF and summary included, enabled."
    )
