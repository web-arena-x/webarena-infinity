import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    original_ids = {f"inv_{i}" for i in range(1, 114)}
    new_invs = [i for i in state["invoices"] if i["id"] not in original_ids]
    if not new_invs:
        return False, "No new invoice found."
    inv = new_invs[0]

    if inv["status"] != "draft":
        return False, f"Expected copy to be 'draft', got '{inv['status']}'"
    orig = next((i for i in state["invoices"] if i["invoiceNumber"] == "INV-0001"), None)
    if not orig:
        return False, "Original invoice INV-0001 not found."
    if inv["contactId"] != orig["contactId"]:
        return False, f"Copy contact mismatch: expected {orig['contactId']}, got {inv['contactId']}"
    return True, "Invoice INV-0001 copied to new draft successfully."
