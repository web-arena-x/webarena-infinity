import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    reminders = state.get("invoiceReminders", [])
    after_reminders = [r for r in reminders if r.get("timing") == "after"]

    if len(after_reminders) == 0:
        return False, "No overdue (after-due-date) invoice reminders found."

    missing_pdf = []
    for r in after_reminders:
        if not r.get("includeInvoicePdf"):
            missing_pdf.append(f"{r.get('days')} day(s) after")

    if missing_pdf:
        return False, (
            f"The following overdue reminders still don't include the invoice PDF: "
            f"{', '.join(missing_pdf)}."
        )

    return True, (
        f"All {len(after_reminders)} overdue invoice reminder(s) now include the invoice PDF."
    )
