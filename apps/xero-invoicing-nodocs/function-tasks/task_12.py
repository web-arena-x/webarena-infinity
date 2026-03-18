import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    inv = next((i for i in state["invoices"] if i["invoiceNumber"] == "INV-0002"), None)
    if not inv:
        return False, "Invoice INV-0002 not found."
    if inv["status"] != "voided":
        return False, f"Expected status 'voided', got '{inv['status']}'"
    if not inv.get("voidedAt"):
        return False, "voidedAt is null."
    return True, "Invoice INV-0002 voided successfully."
