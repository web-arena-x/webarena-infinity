import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("invoiceSettings", {})

    # Check invoice prefix
    if settings.get("invoicePrefix") != "DEMO-":
        return False, f"Expected invoicePrefix 'DEMO-', got '{settings.get('invoicePrefix')}'."

    # Check next number
    if settings.get("invoiceNextNumber") != 100:
        return False, f"Expected invoiceNextNumber 100, got {settings.get('invoiceNextNumber')}."

    # Check default due date: 14 days after invoice date
    due_date = settings.get("defaultDueDate", {})
    if due_date.get("type") != "daysAfterInvoice":
        return False, f"Expected defaultDueDate type 'daysAfterInvoice', got '{due_date.get('type')}'."

    if due_date.get("days") != 14:
        return False, f"Expected defaultDueDate days=14, got {due_date.get('days')}."

    return True, "Invoice settings updated: prefix='DEMO-', next number=100, due date=14 days after invoice."
