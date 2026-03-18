import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    inv = next((i for i in state["invoices"] if i["invoiceNumber"] == "INV-0020"), None)
    if not inv:
        return False, "Invoice INV-0020 not found."
    if inv["dueDate"] != "2026-04-30":
        return False, f"Expected due date '2026-04-30', got '{inv['dueDate']}'"
    return True, "Invoice INV-0020 due date updated correctly."
